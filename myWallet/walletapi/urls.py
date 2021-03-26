from django.conf.urls import url 
from walletapi import views 
 
urlpatterns = [ 
    url(r'^wallet/create$', views.wallet),
    url(r'^wallet/(?P<pk>[0-9]+)$', views.wallet_balance),
    url(r'^transaction/credit$', views.transaction_credit),
    url(r'^transaction/debit$', views.transaction_debit)
]