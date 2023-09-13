from django.urls import path
from . import views

urlpatterns = [
    path('primary_gallery_female/<int:primary_collection_id>/',
         views.get_female_primary_gallery),
    path('secondary_gallery_female/<int:primary_collection_id>/',
         views.get_female_secondary_gallery),
    path('tertiary_gallery_female/<int:primary_collection_id>/',
         views.get_female_tertiary_gallery),
    path('quaternary_gallery_female/<int:primary_collection_id>/',
         views.get_female_quaternary_gallery),
    path('primary_gallery_male/<int:secondary_collection_id>/',
         views.get_male_primary_gallery),
    path('secondary_gallery_male/<int:secondary_collection_id>/',
         views.get_male_secondary_gallery),
    path('tertiary_gallery_male/<int:secondary_collection_id>/',
         views.get_male_tertiary_gallery),
    path('quaternary_gallery_male/<int:secondary_collection_id>/',
         views.get_male_quaternary_gallery),
    path('primary_gallery_other/<int:tertiary_collection_id>/',
         views.get_other_primary_gallery),
    path('secondary_gallery_other/<int:tertiary_collection_id>/',
         views.get_other_secondary_gallery),
]
