from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    course_name = forms.CharField(max_length=100, required=True, help_text='Please enter your course name')

    class Meta:
        model = User
        fields = ('username', 'email', 'course_name' ,'password1', 'password2', )
