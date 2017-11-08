from django import forms
from college.models import Student
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField 
class StudentForm(forms.ModelForm):
    captcha = CaptchaField()    
    class Meta:
        model = Student
        fields = ['name', 'skills', 'sem', 'myimg', 'branch', 'marks_10', 'marks_12', 'marks_aggr']
