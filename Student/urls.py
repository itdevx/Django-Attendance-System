from django.urls import path
from Student import views


app_name = 'student'

urlpatterns = [
    path(
        '', views.IndexView.as_view(), name='index',
    ),
    path(
        'trade', views.TradeView.as_view(), name='trade'
    ),
    path(
        'wallet', views.WalletView.as_view(), name='wallet'
    )
]