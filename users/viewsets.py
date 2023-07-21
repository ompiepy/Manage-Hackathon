from rest_framework import viewsets
from .models import Event, registration_form, submission_form, Result, Mentor, Track, Notification
from .serializers import EventSerializer, RegistrationFormSerializer, SubmissionFormSerializer, ResultSerializer, MentorSerializer, TrackSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegistrationFormViewSet(viewsets.ModelViewSet):
    queryset = registration_form.objects.all()
    serializer_class = RegistrationFormSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SubmissionFormViewSet(viewsets.ModelViewSet):
    queryset = submission_form.objects.all()
    serializer_class = SubmissionFormSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
