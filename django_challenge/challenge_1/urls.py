from django.urls import path
from django.views.generic import TemplateView

from .views import SignupView

urlpatterns = [
    path("inschrijven/", SignupView.as_view(), name="signup"),
    path("bedankt/", TemplateView.as_view(template_name="bedankt.html"), name="signup_thanks"),
]
