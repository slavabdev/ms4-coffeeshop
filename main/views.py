from django.shortcuts import render
from products.models import Category


def main(request):
    '''Returning the index page'''
    return render(request, 'main/index.html')
