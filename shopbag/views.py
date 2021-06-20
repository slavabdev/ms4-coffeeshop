from django.shortcuts import render


def the_bag(request):
    '''Returning the index page'''
    return render(request, 'shopbag/shopbag.html')
