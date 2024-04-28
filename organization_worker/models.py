from django.db import models
from organization.models import Organization
from django.urls import reverse

# Create your models here.
class Organization_Worker(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    worker_title = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    image = models.ImageField(upload_to='photos/organization_worker')
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    gender = (
        (0, 'Select Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender, default=0)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    employment_date = models.DateTimeField()
    terminate_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_user = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)
    is_primary_contact = models.BooleanField(default=False)

    def staff_url(self):
        return reverse('staff_detail', args=[self.id])

    class Meta:
        verbose_name = 'organization_worker'
        verbose_name_plural = 'organization_workers'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
