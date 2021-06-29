from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from products.models import Product
from users.models import UserProfile


@login_required
def favourites(request, product_slug):
    """
    This function allows to add products to favourites
    """
    product = get_object_or_404(Product, slug=product_slug)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)

    return redirect(reverse('product_detail', args=[product.slug]))


@login_required
def favourites_list(request):
    """
    This function renders favourite products
    """
    user = request.user
    favourite_products = user.favourites.all()

    template = 'favourites/favourites_list.html'
    context = {
        'favourite': favourite_products,
    }

    return render(request, template, context)
