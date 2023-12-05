from django.contrib import admin
from .models import (
    PrimaryCollection, 
    SecondaryCollection, 
    TertiaryCollection, 
    CustomerCollection
)

admin.site.register(PrimaryCollection)
admin.site.register(SecondaryCollection)
admin.site.register(TertiaryCollection)
admin.site.register(CustomerCollection)
