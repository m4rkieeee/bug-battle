from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="bugbattle_start.html"), name="bugbattle_start"),
]