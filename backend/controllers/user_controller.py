from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.schemas import *

bp = Blueprint('user', __name__)

@bp.route('/api/otherNonAdminUsers')
@login_required
def getOtherNonAdminUsers():
    users = db.session.query(User).filter((User.id != current_user.id) & (User.is_admin == 0))
    return jsonify(UserSchema(many=True).dump(users))
