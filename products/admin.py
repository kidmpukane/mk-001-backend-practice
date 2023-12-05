from django.contrib import admin
from .models import (
    PrimaryProduct,
    SecondaryProduct, 
    TertiaryProduct
)

admin.site.register(PrimaryProduct)
admin.site.register(SecondaryProduct)
admin.site.register(TertiaryProduct)
