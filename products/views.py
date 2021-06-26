from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm


def all_products(request):
    '''A view to show all products'''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'qry' in request.GET:
            query = request.GET['qry']
            if not query:
                messages.error(request, "Please enter a valid search criteria")
                return redirect(reverse('all_products'))
        
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_slug):
    '''A view to show an individual product details'''
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    '''add a product to th store'''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you have no access to change products!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Item successfully added')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'Item adding failed')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


def edit_product(request, product_slug):
    ''' Edit a product details'''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you have no access to change products!')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item successfully updated')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'Item update failed')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
         'form': form,
         'product': product,
     }

    return render(request, template, context)
