from django.contrib import admin
from .models import Organization_Worker

# Register your models here.
class Organization_WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'worker_title', 'employment_date', 'terminate_date', 'is_user', 'is_management', 'is_primary_contact')
    list_editable = ('is_user', 'is_management', 'is_primary_contact',)
    list_filter = ('worker_title', 'state', 'employment_date', 'gender')

admin.site.register(Organization_Worker, Organization_WorkerAdmin)
