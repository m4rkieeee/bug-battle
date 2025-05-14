from django.views.generic import TemplateView
from challenge_2.models import Training

class TrackOverviewView(TemplateView):
    template_name = "track_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        training_qs = Training.objects.all()
        context["training_qs"] = training_qs
        return context
