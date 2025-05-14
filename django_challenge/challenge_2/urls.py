from django.urls import path
from .views import TrackOverviewView

urlpatterns = [
    path("trainingen/", TrackOverviewView.as_view(), name="track_overview"),
]
