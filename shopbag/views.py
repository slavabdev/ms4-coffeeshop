from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product


def the_bag(request):
    '''Returning the the shopping bag page'''
    return render(request, 'shopbag/shopbag.html')


def add_item_bag(request, item_id):
    ''' add item to the bag '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopbag = request.session.get('shopbag', {})

    if size:
        if item_id in list(shopbag.keys()):
            if size in shopbag[item_id]['items_by_size'].keys():
                shopbag[item_id]['items_by_size'][size] += quantity
            else:
                shopbag[item_id]['items_by_size'][size] = quantity
        else:
            shopbag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shopbag.keys()):
            shopbag[item_id] += quantity
        else:
            shopbag[item_id] = quantity
    request.session['shopbag'] = shopbag
    return redirect(redirect_url)


def update_item_bag(request, item_id):
    ''' update the item quantity in the bag '''
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopbag = request.session.get('shopbag', {})

    if size:
        if quantity > 0:
            shopbag[item_id]['items_by_size'][size] = quantity
        else:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)      
    else:
        if quantity > 0:
            shopbag[item_id] = quantity
        else:
            shopbag.pop(item_id)

    request.session['shopbag'] = shopbag
    return redirect(reverse('the_bag'))


def remove_from_bag(request, item_id):
    '''Remove the specified product to the shopping bag'''

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopbag = request.session.get('shopbag', {})

        if size:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)   
        else: 
            shopbag.pop(item_id)

        request.session['shopbag'] = shopbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)