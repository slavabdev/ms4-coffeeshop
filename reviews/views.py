from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from django.contrib import messages
from products.models import Product
from users.models import UserProfile
from .forms import ReviewForm


def review_list(request, product_slug):

    """function to view the reviews"""

    product = get_object_or_404(Product, slug=product_slug)
    reviews = Review.objects.filter(product=product).order_by('-date_added')
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_review(request, product_slug):

    """to add reviews"""

    if request.user.is_authenticated:
        product = Product.objects.get(slug=product_slug)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.title = request.POST['review_title']
                form.text = request.POST['review_body']
                form.user = UserProfile.objects.get(user=request.user)
                form.product = product
                form.save()
                messages.success(request, 'You successfully added review!')
                return redirect('product_detail', product_slug)
        else:
            form = ReviewForm()
        return redirect(reverse('product_detail', args=(product_slug)))
    else:
        messages.error(request, 'Sorry, only login user can do that.')
        return redirect('main')


@login_required
def edit_review(request, pk):
    """Function to edit reviews"""

    if request.user.is_authenticated:
        review = Review.objects.get(pk=pk)

        if request.user.userprofile == review.user:
            if request.method == 'POST':
                review.review_title = request.POST['review_title']
                review.review_body = request.POST['review_body']
                review.save()
                messages.success(request, 'You successfully edited review!')
                return redirect('product_detail', review.product.slug)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})
        else:
            messages.error(request, 'Sorry, only review owner can do that.')
            return redirect('product_detail')
    else:
        return redirect('main')


@login_required
def delete_review(request, product_slug, review_id):
    """Function to edit reviews"""

    if request.user.is_authenticated:
        product = Product.objects.get(slug=product_slug)
        review = Review.objects.get(product=product, pk=review_id)

        if request.user.is_superuser:
            review.delete()
            messages.success(request, 'You successfully deleted your review!')

        return redirect('product_detail', product_slug)
    else:
        return redirect('main')