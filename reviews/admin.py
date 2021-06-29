from django.contrib import admin
from reviews.models import Review


class ReviewsAdmin(admin.ModelAdmin):
    """
    creates class of review with admin
    """
    list_display = (
        'product',
        'user',
        'date_added',
        'review_title',
        'review_body',
    )

admin.site.register(Review, ReviewsAdmin)