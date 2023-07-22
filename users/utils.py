from nltk.corpus import stopwords
from .models import registration_form, Mentor
from django.core.mail import send_mail
from django.conf import settings
from .helpers import compare_similarity


def sending_mail(subject, message, recepient):
    sent_from = settings.DEFAULT_FROM_EMAIL
    return send_mail(subject, message, sent_from, recipient_list=[recepient])


def match_mentor_and_team():
    teams = registration_form.objects.filter(for_event__is_active=True)
    mentors = Mentor.objects.filter(for_event__is_active=True)

    for team in teams:
        for mentor in mentors:
            # process_mentor_expertise = preprocess(mentor.expertise)
            # process_data_team = preprocess(team.project_description)
            similarity = compare_similarity(
                team.tools_to_be_used, mentor.expertise)
            if (similarity > 0.30):
                team.mentor = mentor
                team.save()


# def assign_room():
#     teams = registration_form.objects.all()
#     similar = {}
#     for teama in teams:
#         for teamb in teams:
#             similarity = compare_similarity(
#                 teama.tools_to_be_used, teamb.tools_to_be_used)
#             if (similarity > 0.30):
#                 similar += {teama, teamb}
#             else:
#                 disimilar = {}
