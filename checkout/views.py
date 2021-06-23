from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopbag = request.session.get('shopbag', {})
    if not shopbag:
        messages.error(request, 'Your bag is empty')
        return redirect(reverse('all_products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
