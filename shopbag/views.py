from django.shortcuts import render,redirect


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
