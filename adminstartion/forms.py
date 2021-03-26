from django import forms
from django.contrib.auth import authenticate, get_user_model
from user.models import Student
from ubook_lms import settings


User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'type'

        ]
        

class StudentAddForm(forms.ModelForm):

    birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    
    class Meta:
        model = Student
        exclude = ['user']