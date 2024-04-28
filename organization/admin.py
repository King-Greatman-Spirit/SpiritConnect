from django.contrib import admin
from .models import Organization, OrganizationOverview

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'created_date', 'state', 'modified_date', 'is_church')
    list_editable = ('is_church',)
    list_filter = ('organization_name', 'state', 'modified_date')

class OrganizationOverviewAdmin(admin.ModelAdmin):
    list_display = ('organization',)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationOverview, OrganizationOverviewAdmin)
