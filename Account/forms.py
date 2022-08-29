from django import forms


class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-control', 'placeholder':'Password'}))
    