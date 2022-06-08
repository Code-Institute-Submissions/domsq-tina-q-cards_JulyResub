from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ View to allow checkout """

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPR59DBDb81Ckg7NywCTbB90lSoI2R3NRX'
                             'YvXOMjLLSKspJHxfm5WjESwGCMmBtJ'
                             'tVsdGiFtIKNSzKbvKhydJhh00cx12qnqh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
