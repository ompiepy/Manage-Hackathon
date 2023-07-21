from rest_framework import serializers
from .models import Event, registration_form, submission_form, Result, Mentor, Track, Notification


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration_form
        fields = '__all__'


class SubmissionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = submission_form
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
