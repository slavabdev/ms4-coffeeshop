from django.shortcuts import render

def main(request):
    '''Returning the index page'''
    return render(request, 'main/index.html')
