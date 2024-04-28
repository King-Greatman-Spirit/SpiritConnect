from django.contrib import admin
from .models import Preacher

# Register your models here.
class PreacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'created_date', 'is_worker', 'is_active')
    list_editable = ('is_worker', 'is_active',)
    list_filter = ['first_name']
    list_per_page = 20



admin.site.register(Preacher, PreacherAdmin)
