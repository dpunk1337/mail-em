from flask import Blueprint, jsonify, request
from backend.services import MailService, UserService
bp = Blueprint('mail', __name__)


@bp.route('/api/schedule-mail', methods=['POST'])
def schedule_mail():
    mail = {
        'subject': request.form.get('subject'),
        'message': request.form.get('message')
    }
    sender_email_id = request.form.get('sender_id')
    receiver_email_id = request.form.get('receiver_id')

    sender = UserService.get_user_by_email(sender_email_id)
    receiver = UserService.get_user_by_email(receiver_email_id)

    MailService.schedule_mail(sender, mail, receiver)
    return jsonify({'mail': mail, 'sender_email_id': sender_email_id, 'receiver_email_id': receiver_email_id})
