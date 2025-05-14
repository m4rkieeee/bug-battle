from django.views.generic import TemplateView

from challenge_4.models import EvaluationQuestion


class EvaluationView(TemplateView):
    template_name = "evaluations/evaluate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson_id = self.request.GET.get("lesson")

        # SELECT * FROM evaluation_evaluationquestion WHERE active = TRUE;
        context["questions"] = EvaluationQuestion.objects.filter(active=True)
        return context
