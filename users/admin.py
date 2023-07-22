from django.contrib import admin
from .models import registration_form, submission_form, Result, Event, Mentor, Notification, Judges, NotificationRecipient

# Register your models here.
admin.site.register(registration_form)
admin.site.register(submission_form)
admin.site.register(Result)
admin.site.register(Event)
admin.site.register(Mentor)
admin.site.register(Notification)
admin.site.register(NotificationRecipient)
admin.site.register(Judges)
