from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SignupForm

class SignupView(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("signup_thanks")

    def form_valid(self, form):
        # Hier zou je de inschrijving opslaan of e-mailen
        print("Inschrijving ontvangen:", form.cleaned_data)
        return super().form_valid(form)
