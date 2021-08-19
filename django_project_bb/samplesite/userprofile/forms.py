from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')