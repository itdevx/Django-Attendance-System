from cmath import log
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Account import forms
from Account.forms import UserRegistrationForm
from django.urls import reverse_lazy


class LoginView(generic.View):
    template_name = 'signin.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = request.POST.get('reme')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('student:index')

            else:
                form.add_error(field='username', error='نام کاربری یا کلمه عبور اشتباه میباشد!')

        return render(request, self.template_name, {'form': form})


class LogoutRequest(generic.View):
    def get(self, request):
        logout(request)
        return redirect('account:login')


class SignUpView(generic.CreateView):
    template_name = 'create-user.html'
    success_url = reverse_lazy('student:created-list')
    form_class = UserRegistrationForm
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


        