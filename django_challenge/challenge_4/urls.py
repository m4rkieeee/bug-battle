from django.urls import path

from challenge_4.views import EvaluationView

urlpatterns = [
    path('questions/', EvaluationView.as_view(), name='questions'),
]