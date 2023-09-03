from cmath import log
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Account import forms
from Account.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Student import mixins



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


class SignUpView(mixins.SuperUserAccessMixins, LoginRequiredMixin, generic.CreateView):
    login_url = 'account:login'
    template_name = 'create-user.html'
    success_url = reverse_lazy('student:created-list')
    form_class = UserRegistrationForm
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = User.objects.all()
        return context


class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'account:login'
    template_name = 'update-user.html'
    context_object_name = 'form'
    model = User
    form_class = forms.UpdateUserForm
    success_url = reverse_lazy('student:index')
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return User.objects.get(username=username)
