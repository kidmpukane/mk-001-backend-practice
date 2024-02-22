from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('user_profiles.urls')),
    path('api/', include('store.urls')),
    path('api/store/', include('store_collections.urls')),
    # path('api/store/gallery/', include('store_galleries.urls')),
    path('api/products/', include('products.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
