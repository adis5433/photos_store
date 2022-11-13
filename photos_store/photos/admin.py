from django.contrib import admin

# Register your models here.
from photos.models import Photo, Album





class PhotoAdmin(admin.ModelAdmin):
   list_display = ['id', 'title', 'image', 'album']
   list_filter = ['title' , 'album']
   search_fields = ['title']

class AlbumAdmin(admin.ModelAdmin):
   list_display = ['album_title']
   list_filter = ['album_title']
   search_fields = ['album_title']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)