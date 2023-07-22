from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# email needed to be sent after user creation


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    time = models.DateField()
    registration_required = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    mentor_name = models.CharField(max_length=255)
    expertise = models.TextField()
    contact = models.CharField(max_length=15)
    available_time = models.TextField()
    for_event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.mentor_name


class Judges(models.Model):
    Judge_name = models.CharField(max_length=255)
    background = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    for_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    judge_registration = models.OneToOneField(User, on_delete=models.CASCADE,
                                              related_name='Judges', null=True, blank=True)

    def __str__(self):
        return self.Judge_name


class registration_form(models.Model):
    team_name = models.CharField(max_length=255)
    leader_name = models.CharField(max_length=255)
    member_2 = models.CharField(max_length=255)
    member_3 = models.CharField(max_length=255, null=True, blank=True)
    member_4 = models.CharField(max_length=255, null=True, blank=True)
    leader_contact = models.CharField(max_length=15)
    leader_email = models.EmailField()
    project_idea = models.CharField(max_length=255)
    project_description = models.TextField(null=True, blank=True)
    tools_to_be_used = models.TextField()
    anything_else = models.TextField()
    prvious_projects = models.URLField()
    for_event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    user_registration = models.OneToOneField(User, on_delete=models.CASCADE,
                                             related_name='registration_form', null=True, blank=True)
    mentor = models.ForeignKey(
        Mentor, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.team_name


class submission_form(models.Model):
    team_name = models.ForeignKey(User, on_delete=models.CASCADE)
    git_repo = models.URLField()
    drive_link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.team_name.username


class Result(models.Model):
    team_name = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    suggestion = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return f'{self.team_name}-{self.points}'


class Track(models.Model):
    team = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()

    def __str__(self):
        return self.team.username


class Notification(models.Model):
    main_heading = models.CharField(max_length=255)
    information = models.TextField()
    recipients = models.ManyToManyField(
        User, through='NotificationRecipient', related_name='notifications')

    def __str__(self):
        return self.main_heading


class NotificationRecipient(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any additional fields if needed, such as a flag to mark if the notification has been read by the user.

    def __str__(self):
        return f"{self.notification.main_heading} - {self.user.username}"


class ReviewForm(models.Model):
    team_name = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()

    def __str__(self):
        return self.team_name
# Review Form
# notification for some and all
