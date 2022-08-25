from http.client import RemoteDisconnected
from django.shortcuts import render
from django.views import generic


class LoginView(generic.View):
    def get(self, request):
        
        return render(request, 'signin.html')


class SignUpView(generic.View):
    def get(self, request):
        return render(request, 'signup.html')
        