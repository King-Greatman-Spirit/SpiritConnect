from django.contrib import admin
from .models import Gallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'organization', 'created_date', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Gallery, GalleryAdmin)
