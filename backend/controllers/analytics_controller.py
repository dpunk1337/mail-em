from flask import Blueprint, jsonify
from backend.services import MailService

bp = Blueprint('analytics', __name__)


@bp.route('/api/mail-analytics')
def get_mail_analytics():
    data = {
        'scheduled' : MailService.get_number_of_scheduled_mails(),
        'sent' : MailService.get_number_of_sent_mails(),
        'opened' : MailService.get_number_of_opened_mails()
    }
    return jsonify(data)
