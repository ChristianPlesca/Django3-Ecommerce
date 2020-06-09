from django.shortcuts import render

def cart_contents(request):
    return render(request,'cart/cart.html')
