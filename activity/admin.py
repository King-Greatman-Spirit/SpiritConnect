from django.contrib import admin
from .models import Activity, Activity_Type, Testimony

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('activity_name',)}
    list_display = ('activity_name', 'slug', 'state', 'created_date', 'is_active')
    list_editable = ('is_active',)

class Activity_TypeAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'created_date', 'modified_date', 'is_active')
    list_editable = ('is_active',)

class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('testimony_title', 'city', 'state', 'country', 'is_active')
    list_editable = ('is_active',)
    list_per_page = 20


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Activity_Type, Activity_TypeAdmin)
admin.site.register(Testimony, TestimonyAdmin)
