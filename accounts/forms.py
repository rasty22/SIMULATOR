from django import forms  # type: ignore[reportMissingModuleSource]
from django.contrib.auth.forms import UserCreationForm #type: ignore 
from accounts.models import Profile
from django.contrib.auth.models import User  # type: ignore

class SignUPForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)


    class Meta:
        model = User
        fields = ['username', 'email',]

def save(self,commit=True):
        user = super().save(commit=commit)
        if commit:
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
            return user