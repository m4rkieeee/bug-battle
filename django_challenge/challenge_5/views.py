from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

BugView = TemplateView.as_view(template_name='challenge_5.html')