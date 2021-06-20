from django.shortcuts import render
from products.models import Category


def main(request):
    '''Returning the index page'''
    categories = Category.objects.all()
    

    context = {
        'categories': categories,
        
    }
    

    return render(request, 'main/index.html', context)
