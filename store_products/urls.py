from django.urls import path
from . import views

urlpatterns = [
    path('product_view/<int:store_gallery_id>', views.get_primary_product)
]
