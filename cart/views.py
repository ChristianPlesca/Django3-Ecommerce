from django.shortcuts import render,redirect

def cart(request):
    return render(request,'cart/cart.html')


def add_to_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    """ we first check to see if there is a cart variable if not we create one """
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)
