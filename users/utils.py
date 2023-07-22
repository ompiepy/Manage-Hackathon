from nltk.corpus import stopwords
from .models import registration_form, Mentor
from django.core.mail import send_mail
from django.conf import settings




def sending_mail(subject, message, recepient):
    sent_from = settings.DEFAULT_FROM_EMAIL
    return send_mail(subject, message, sent_from, recipient_list=[recepient])


def match_mentor_and_team(team_name, mentor_name):
    team = registration_form.objects.get(team_name=team_name)
    mentor = Mentor.objects.get(mentor_name=mentor_name)

    # if (team.)
    pass
