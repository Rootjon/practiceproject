from django.contrib import admin

from .models import Album
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display =[
        'description',
        'description',
        'creation',
    ]

admin.site.register(Album, AlbumAdmin)

