from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_profiles.urls')),
    path('api/', include('store.urls')),
    path('api/store/', include('store_collections.urls')),
    path('api/store/gallery', include('store_galleries.urls')),
    path('api/products', include('store_products.urls')),

]
