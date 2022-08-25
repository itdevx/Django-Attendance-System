from django.shortcuts import redirect, render
from django.views import generic




class IndexView(generic.View):
    def get(self, request):

        return render(request, 'index.html')

    
class TradeView(generic.View):
    def get(self, request):

        return render(request, 'trade.html')


class WalletView(generic.View):
    def get(self, request):

        return render(request, 'wallet.html')