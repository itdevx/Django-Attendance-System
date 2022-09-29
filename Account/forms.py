from django import forms


class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder':'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-control', 'placeholder':'رمز عبور'}))
    