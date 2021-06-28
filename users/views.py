from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from checkout.models import Order


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    orders_count = orders.count()

    template = 'users/profile.html'
    context = {
        'profile': profile,
        'orders_count': orders_count,

    }
    return render(request, template, context)


def update_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.POST:
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profile successfully updated!')
        else:
            messages.error(request, 'Profile update is Failed')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'users/update_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


def all_order_history(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'users/all_order_history.html'
    context = {
        'profile': profile,
        'orders': orders

    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f'This is  past confirmation for \
                            order number {order_number}.'
                            'A confirmation was sent on the order date'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
