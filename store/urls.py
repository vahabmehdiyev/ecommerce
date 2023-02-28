from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.card, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    

]