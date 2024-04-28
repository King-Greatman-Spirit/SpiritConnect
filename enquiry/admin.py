from django.contrib import admin
from .models import ContactForm
# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'job_title','channel', 'subject')
    list_per_page = 20

admin.site.register(ContactForm, ContactFormAdmin)
