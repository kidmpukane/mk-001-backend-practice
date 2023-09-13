from django.contrib import admin
from .models import FemalePrimaryGallery, FemaleSecondaryGallery, FemaleTertiaryGallery, FemaleQuaternaryGallery, \
    MalePrimaryGallery, MaleSecondaryGallery, MaleTertiaryGallery, MaleQuaternaryGallery, \
    OtherPrimaryGallery, OtherSecondaryGallery

admin.site.register(FemalePrimaryGallery)
admin.site.register(FemaleSecondaryGallery)
admin.site.register(FemaleTertiaryGallery)
admin.site.register(FemaleQuaternaryGallery)
admin.site.register(MalePrimaryGallery)
admin.site.register(MaleSecondaryGallery)
admin.site.register(MaleTertiaryGallery)
admin.site.register(MaleQuaternaryGallery)
admin.site.register(OtherPrimaryGallery)
admin.site.register(OtherSecondaryGallery)
