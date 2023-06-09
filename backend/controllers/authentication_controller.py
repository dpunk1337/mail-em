from flask import Blueprint, request, jsonify, abort
from flask_login import login_user, login_required, logout_user, current_user
from backend import login_manager
from backend.models import User
from backend.forms import *
from backend.schemas import UserSchema
from functools import wraps
from backend.services import UserService

bp = Blueprint('authentication',__name__)

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return func(*args, **kwargs)
    return decorated_view

@bp.route('/api/login', methods=['POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
        return jsonify({'success': False, 'message':'Invalid credentials'}), 403
    login_user(user, remember=form.remember_me.data)
    logged_in_user = UserSchema().dump(user)
    logged_in_user.pop('password')
    return jsonify({'success': True, 'message': 'Login successful', 'user': logged_in_user})

@bp.route('/api/signup', methods=['POST'])
def signup():
    user = {
        'first_name' : request.form['firstName'],
        'last_name' : request.form['lastName'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'is_admin' : request.form['is_admin'] if 'is_admin' in request.form else False
    }
    print(user)
    UserService.add_user(user)
    return jsonify({'success': True, 'message': 'Sign up successful'})


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_required
@bp.route('/api/logout',methods=['GET'])
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})


@bp.route('/api/is_authenticated', methods=['GET'])
@login_required
def is_authenticated():
    user = User.query.get(int(current_user.userid))
    logged_in_user = UserSchema().dump(user)
    logged_in_user.pop('password')
    return jsonify({'is_authenticated': True, 'user': logged_in_user})
