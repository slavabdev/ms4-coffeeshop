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
        'stripe_public_key': 'pk_test_51Ixi2pKz2mpITkQXeE15AZzMm9rilj2Get0WWFDX1g0NmOVn2vQaamXIY0omFSlEyS8yEzpufiX8sWFlFuSsqUMQ00yEjMYg0f',
        'client_secret' : 'test client secret'
    }

    return render(request, template, context)
