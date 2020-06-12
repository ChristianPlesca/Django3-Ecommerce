from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_q4o8w3CrmWjVoEaNg2sCMxx900pWCBqSLs',
        'client_secret':'sk_test_49jlYJQZ6hND57wBTdtcqRG900jvacvwgU'
    }

    return render(request, template, context)