from .models import Login, Registration
from django.forms import ModelForm, TextInput,PasswordInput


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ["username","password"]
        widgets = {
            "username": TextInput(attrs={
                'placeholder':"Enter your username",
                'style':'width: 300px;height: 45px;border-radius: 10px;font-size: 20px;margin-left: 25%;margin-top : 50px;'
            }),
            "password": TextInput(attrs={
               'placeholder':"Enter your password",
               'style':'width: 300px;height: 45px;border-radius: 10px;font-size: 20px;margin-left: 25%;margin-top : 50px;'
            }),
        }

        
class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["username","password"]
        widgets = {
            "username": TextInput(attrs={
                'placeholder':"Enter your username",
                'style':'width: 300px;height: 45px;border-radius: 10px;font-size: 20px;margin-left: 25%;margin-top : 50px;'
            }),
            "password": PasswordInput(attrs={
               'placeholder':"Enter your password",
               'style':'width: 300px;height: 45px;border-radius: 10px;font-size: 20px;margin-left: 25%;margin-top : 50px;'
            }),
        }
