from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder':'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-control', 'placeholder':'کلمه عبور'}))


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.IntegerField()
        self.fields['username'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام کاربری را وارد کنید (کد ملی)'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام را وارد کنید'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام خانوادگی را وارد کنید'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'گذر واژه را وارد کنید'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'گذره وازه را دوباره وارد کنید'})

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password1', 'password2'
        ]
