from django import views
from django.urls import path
from Account import views

app_name = 'account'

urlpatterns = [
    path(
        'login/', views.LoginView.as_view(), name='login'
    ),
    path(
        'register', views.SignUpView.as_view(), name='register'
    )
]