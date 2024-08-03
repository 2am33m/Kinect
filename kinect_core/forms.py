from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Photo, Reel

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'photo_path']

class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ['description', 'video']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search other users')