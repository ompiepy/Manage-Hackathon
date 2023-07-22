from .models import registration_form
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .utils import sending_mail


@receiver(post_save, sender=registration_form)
def create_user(sender, instance, created, **kwargs):
    """
    A signal receiver function to create a new user when a RegistrationForm instance is saved.
    """
    if created:
        # Create a new user with the team_name as the username and '12345' as the default password
        try:
            word = get_random_string(10)
            username_processing = 'Team-' + instance.team_name
            user = User.objects.create(
                username=username_processing, email=instance.leader_email)
            instance.user_registration = user
            instance.save()
            user.set_password(word)
            user.save()
            Subject = "Welcome and Credentials"
            message = '''Welcome to the Hackathon. Here is your hackathon credentials that you will be using
                        through out the event'''+f'''
                            username: {user.username}\n password: {word}\n'''
            recepient = user.email
            sending_mail(Subject, message, recepient)
            return
        except:
            return "Error Occoured"
