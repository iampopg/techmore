from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib import messages


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.CharField(max_length=50, required=True,)
    

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
        ]
    # def uniqueError(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():  #for email unique validatory
            
    #         # raise ValidationError("Email has already Exists")
    #         return self.cleaned_data


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class profileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False, label="PROFILE PHOTO")
    # DOB = forms.DateTimeField(required=True)
    # gender = forms.CharField(widget=forms.RadioSelect, required=False)
    # staff = forms.widgets()
    class Meta:
        model = Profile
        fields = [
            'profile_photo',
            'idea_type',
            'purpose',
            'DOB',
            'address',
            'gender',
            'phone_number',
        ]
    # widgets = {

    #         'DOB': forms.NumberInput(attrs={'type':'date'}),
    #         }