from django.shortcuts import render
from products.models import Category, Product


def main(request):
    '''Returning the index page'''
    products = Product.objects.all()
    categories = Category.objects.all()

    if 'categories':
        categories = categories.filter(name__in=categories)   
    context = {
        'categories': categories,
        'products': products,
        }

    return render(request, 'main/index.html', context)
