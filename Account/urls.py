from django import views
from django.urls import path
from Account import views

app_name = 'account'

urlpatterns = [
    path(
        'login/', views.LoginView.as_view(), name='login'
    ),
    path(
        'create-user', views.SignUpView.as_view(), name='create-user'
    ),
    path(
        'logout', views.LogoutRequest.as_view(), name='logout'
    ),
]