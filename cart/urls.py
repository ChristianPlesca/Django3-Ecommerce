from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_contents, name='cart_contents')
]
