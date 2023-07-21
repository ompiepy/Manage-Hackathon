from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventViewSet, RegistrationFormViewSet, SubmissionFormViewSet, ResultViewSet, MentorViewSet, TrackViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'registration_forms', RegistrationFormViewSet)
router.register(r'submission_forms', SubmissionFormViewSet)
router.register(r'results', ResultViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
