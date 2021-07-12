from django.contrib import admin
from.models import Slider, Feature

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display=[
        'headline',
        'thumbnail',
        'short_description',

    ]
admin.site.register (Slider, SliderAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display=[
        'haedline',
        'thumbnail',
        'slug',
        'description',
        'creation'


    ]
admin.site.register (Feature, FeatureAdmin)   