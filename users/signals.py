from .models import registration_form, Notification, Judges
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.utils.crypto import get_random_string
from .utils import sending_mail
from .models import Event


@receiver(post_save, sender=registration_form)
def create_user(sender, instance, created, **kwargs):
    """
    A signal receiver function to create a new user when a RegistrationForm instance is saved.
    """
    if created:
        # Create a new user with the team_name as the username and '12345' as the default password
        try:
            word = get_random_string(10)
            event = Event.objects.get(is_active=True)
            username_processing = 'Team-' + instance.team_name
            user = User.objects.create(
                username=username_processing, email=instance.leader_email)
            instance.user_registration = user
            if instance.for_event is None:
                instance.for_event = event
            instance.save()
            user.set_password(word)
            user.save()
            add_result_permission = Permission.objects.get(
                codename='add_submission_form')
            add_view_result_permission = Permission.objects.get(
                codename='view_result')
            add_view_event_permission = Permission.objects.get(
                codename='view_event')
            user.user_permissions.add(add_result_permission)
            user.user_permissions.add(add_view_result_permission)
            user.user_permissions.add(add_view_event_permission)

            Subject = "Welcome and Credentials"
            message = '''Welcome to the Hackathon. Here is your hackathon credentials that you will be using
                        through out the event'''+f'''
                            \n username: {user.username}\n password: {word}\n'''
            recepient = user.email
            sending_mail(Subject, message, recepient)
            return
        except:
            return "Error Occoured"


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        teams = registration_form.objects.all()
        subject = instance.main_heading
        message = instance.information
        for team in teams:
            sending_mail(subject, message, team.leader_email)


@receiver(post_save, sender=Judges)
def create_judge_account(sender, instance, created, **kwargs):
    if created:
        try:
            word = get_random_string(10)
            username_processing = 'Judge-' + instance.Judge_name
            user = User.objects.create(
                username=username_processing, email=instance.email)
            instance.judge_registration = user
            instance.save()
            user.set_password(word)
            user.save()
            add_result_permission = Permission.objects.get(
                codename='add_result')
            update_result_permission = Permission.objects.get(
                codename='change_result')
            delete_result_permission = Permission.objects.get(
                codename='delete_result')
            user.user_permissions.add(add_result_permission)
            user.user_permissions.add(update_result_permission)
            user.user_permissions.add(delete_result_permission)
            Subject = "Welcome and Credentials"
            message = '''Welcome to the Hackathon. Here is your hackathon credentials that you will be using
                        through out the event'''+f'''
                            \n username: {user.username}\n password: {word}\n'''
            recepient = user.email
            sending_mail(Subject, message, recepient)
            return ('Nice!')
        except:
            return "Error Occoured!"
