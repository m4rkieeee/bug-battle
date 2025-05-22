from django.urls import path

from challenge_5.views import BugView

urlpatterns = [
    path('game/', BugView, name='challenge_5'),
]