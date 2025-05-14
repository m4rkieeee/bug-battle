from django.urls import path

from challenge_4.views import EvaluationView

urlpatterns = [
    path('questons/', EvaluationView.as_view(), name='questions'),
]