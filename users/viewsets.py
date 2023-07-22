from rest_framework import viewsets
from .models import Event, registration_form, submission_form, Result, Mentor, Track, Notification
from .serializers import EventSerializer, RegistrationFormSerializer, SubmissionFormSerializer, ResultSerializer, MentorSerializer, TrackSerializer, NotificationSerializer
from rest_framework import permissions
from .permissions import RegistrationPermission, SubmissionPermission, GeneralPermission


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [GeneralPermission]


class RegistrationFormViewSet(viewsets.ModelViewSet):
    queryset = registration_form.objects.all()
    serializer_class = RegistrationFormSerializer
    permission_classes = [RegistrationPermission]


class SubmissionFormViewSet(viewsets.ModelViewSet):
    queryset = submission_form.objects.all()
    serializer_class = SubmissionFormSerializer
    permission_classes = [SubmissionPermission]


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAdminUser]


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [SubmissionPermission]


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAdminUser]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]
