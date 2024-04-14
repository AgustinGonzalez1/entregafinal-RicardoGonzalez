from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.Form):
  name = forms.CharField(max_length = 45)
  commission = forms.IntegerField()
  course = forms.CharField(max_length = 45)


class TeacherForm(forms.Form):
  name = forms.CharField(max_length = 45)
  course_name = forms.CharField(max_length = 45)


class CourseForm(forms.Form):
  name = forms.CharField(max_length = 45)
  teacher = forms.CharField(max_length = 45)


class UserEditForm(UserCreationForm):

  email = forms.EmailField()
  password1 = forms.CharField()
  password2 = forms.CharField()
  