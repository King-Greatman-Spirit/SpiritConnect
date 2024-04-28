from django.db import models

# Create your models here.
class Organization(models.Model):
    organization_name = models.CharField(max_length=100, default=True)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='photos/organizations', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_church = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    service_invite = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.organization_name

class OrganizationOverview(models.Model):
    organization = models.OneToOneField(
        Organization,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    mandate = models.TextField(max_length=500, blank=True)
    mission_statement = models.TextField(max_length=500, blank=True)
    vision = models.TextField(max_length=500, blank=True)
    philosophy = models.TextField(max_length=500, blank=True)
    population = models.TextField(max_length=500, blank=True)
    branch = models.TextField(max_length=500, blank=True)
    Cell_fellowship = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.organization.organization_name
