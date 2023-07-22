
from django.core.mail import send_mail
from django.conf import settings


def sending_mail(subject, message, recepient):
    sent_from = settings.DEFAULT_FROM_EMAIL
    return send_mail(subject, message, sent_from, recipient_list=[recepient])
