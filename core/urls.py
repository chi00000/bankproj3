from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.api_login),
    path('logout/', views.api_logout),

    path('accounts/', views.AccountListView.as_view()),
    path('payees/', views.PayeeListView.as_view()),
    path('transfer/', views.transfer_to_payee),
    path('transactions/', views.TransactionListView.as_view()),
]
