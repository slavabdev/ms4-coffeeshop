from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def user(request):
    '''
    Display user profile
    '''
    template = 'users/user.html'
    context = {}

    return render(request, template, context)
