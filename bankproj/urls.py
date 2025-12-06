from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.transaction_page, name='transaction'),
    path('transfer/', views.transfer_page, name='transfer'),
    path('register/', views.register, name='register'),

    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

