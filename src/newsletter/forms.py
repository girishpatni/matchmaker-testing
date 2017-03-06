from django import forms

from .models import SignUp

class SignUpForm(forms.modelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
    def clean_email(self):
        """Custome Email Validator"""
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError("Please use a valid college email address")
        return email