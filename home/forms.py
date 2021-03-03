from django.forms import ModelForm, DateField
from user.models import Student
from ubook_lms import settings


class StudentForm(ModelForm):

    birth = DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    
    class Meta:
        model = Student
        fields = '__all__'





