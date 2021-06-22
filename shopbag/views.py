from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages


def the_bag(request):
    '''Returning the the shopping bag page'''
    return render(request, 'shopbag/shopbag.html')


def add_item_bag(request, item_id):
    ''' add item to the bag '''

    product = get_object_or_404(Product, slug=item_id)

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
                messages.success(request, f'Updated size {size} {product.name} quantity to {shopbag[item_id]["items_by_size"][size]}')
            else:
                shopbag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'{size} {product.name} added to your cart')
        else:
            shopbag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'{size} {product.name} added to your cart')
    else:
        if item_id in list(shopbag.keys()):
            shopbag[item_id] += quantity
            messages.success(request, f' Updated {product.name} quantity to {shopbag[item_id]}')
        else:
            shopbag[item_id] = quantity
            messages.success(request, f'{product.name} added to your cart.')
    request.session['shopbag'] = shopbag
    return redirect(redirect_url)


def update_item_bag(request, item_id):
    ''' update the item quantity in the bag '''

    product = get_object_or_404(Product, slug=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopbag = request.session.get('shopbag', {})

    if size:
        if quantity > 0:
            shopbag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size} {product.name} quantity to {shopbag[item_id]["items_by_size"][size]}')

        else:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)
            messages.success(request, f'{size} {product.name} removed from your cart')      
    else:
        if quantity > 0:
            shopbag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {shopbag[item_id]}')
        else:
            shopbag.pop(item_id)
            messages.success(request, f'{product.name} removed from your bag')

    request.session['shopbag'] = shopbag
    return redirect(reverse('the_bag'))


def remove_from_bag(request, item_id):
    '''Remove the specified product to the shopping bag'''

    try:
        product = get_object_or_404(Product, slug=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopbag = request.session.get('shopbag', {})

        if size:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)
            messages.success(request, f'{size} {product.name} removed from your bag')   
        else: 
            shopbag.pop(item_id)
            messages.success(request, f'{product.name} removed from your bag')

        request.session['shopbag'] = shopbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)