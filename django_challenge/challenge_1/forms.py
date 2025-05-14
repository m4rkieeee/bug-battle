from django import forms

class SignupForm(forms.Form):
    naam = forms.CharField(
        label="Voornaam",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Voornaam"
        })
    )
    email = forms.EmailField(
        label="E-mailadres",
        widget=forms.EmailInput(attrs={
            "class": "w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "E-mailadres"
        })
    )
