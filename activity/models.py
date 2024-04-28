from django.db import models
from organization.models import Organization
from preacher.models import Preacher
from smart_selects.db_fields import ChainedForeignKey
# from django.urls import reverse

# Create your models here.
class Activity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100, default=True)
    slug = models.SlugField(max_length=100, unique=True)
    activity_description = models.TextField(max_length=500, blank=True)
    duration = models.CharField(max_length=50, default=True)
    image = models.ImageField(upload_to='photos/activities')
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    activity_preacher = models.ManyToManyField(Preacher)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.activity_name

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'



class Activity_Type(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    activity = ChainedForeignKey(
        Activity,
        chained_field="organization",
        chained_model_field="organization",
        show_all = False,
        auto_choose=True,
        default=None)
    activity_type = models.CharField(max_length=50)
    # description = models.TextField(max_length=300)
    # image = models.ImageField(upload_to='photos/activity_type')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'ActivityType'
        verbose_name_plural = 'Activity Types'

    def __str__(self):
        return self.activity_type



class Testimony(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=True)
    activity = ChainedForeignKey(
        Activity,
        chained_field="organization",
        chained_model_field="organization",
        show_all = False,
        auto_choose=True,
        default=None)
    testimony_title = models.CharField(max_length=100)
    testimony_description = models.TextField(max_length=300)
    testimony_image = models.ImageField(upload_to='photos/activity_type', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    testifier_name = models.CharField(max_length=100, default=True)
    city = models.CharField(max_length=50, default=True)
    state = models.CharField(max_length=50, default=True)
    country = models.CharField(max_length=50, default=True)

    class Meta:
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.activity_type
