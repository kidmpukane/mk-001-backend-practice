from django.contrib import admin
from .models import PrimaryCollection, SecondaryCollection, TertiaryCollection

admin.site.register(PrimaryCollection)
admin.site.register(SecondaryCollection)
admin.site.register(TertiaryCollection)
