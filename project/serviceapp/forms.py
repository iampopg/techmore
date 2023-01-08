from django import forms
from .models import message, uploadIdea, bugsModel


class messageForm(forms.ModelForm):
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    messages = forms.CharField(required= True)
    email = forms.EmailField(required=True)
    class Meta:
        model = message
        fields = [
            'first_name',
            'last_name',
            'email',
            'messages',
            
        ]

class uploadForm(forms.ModelForm):
    fileToUpload = forms.FileField( max_length= 225, required=True)
    # pincode = forms.CharField(required=True)
    class Meta:
        model = uploadIdea
        fields = [
            'purpose',
            'worth',
            'email',
            'description',
            'fileToUpload',
        ]

class statusForm(forms.ModelForm):
    class Meta:
        model = uploadIdea
        fields = [
            'email',
            'pincode'
        ]
class decideForm(forms.ModelForm):
    class Meta:
        model = uploadIdea
        fields = [
            'payment',
            'status',
        ]
class bugForm(forms.ModelForm):
    
    # bug_name = forms.CharField(choice=social_media, required=True)
    class Meta:
        model = bugsModel
        fields= [
            'bug_type',
            'bug_name',
            'email',
            'description'
        ]

