from django import forms
from django.contrib.auth.forms import UserCreationForm

from CrudApp.models import Login, Student


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)

