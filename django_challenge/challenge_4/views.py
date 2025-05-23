from django.views import View
from django.shortcuts import render, redirect
from challenge_4.models import EvaluationQuestion, EvaluationStudentAnswer
from django.urls import reverse_lazy



class EvaluationView(View):
    template_name = "evaluations/evaluate.html"

    def get(self, request):
        lesson_id = self.request.GET.get("lesson")
        # SELECT * FROM evaluation_evaluationquestion WHERE active = TRUE;
        questions = EvaluationQuestion.objects.filter(active=True)
        return render(self.request, self.template_name, {
            'questions': questions,
            'lesson_id': lesson_id,
        })

    def post(self, request):
        for key, value in request.POST.items():
            if key.startswith("q"):
                question_id = key[1:]
                question = EvaluationQuestion.objects.get(id=question_id)
                answer = EvaluationStudentAnswer.objects.create(
                    question=question,
                    answer=value,
                    student=self.request.user,
                )
                print(answer)
                answer.save()
        return redirect(reverse_lazy('questions'))