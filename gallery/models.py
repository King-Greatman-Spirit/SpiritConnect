from django.db import models
from organization.models import Organization
# from activity.models import Activity
# from smart_selects.db_fields import ChainedForeignKey
from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=True)
    # activity = ChainedForeignKey(
    #     Activity,
    #     chained_field="organization",
    #     chained_model_field="organization",
    #     show_all = False,
    #     auto_choose=True,
    #     default=None)
    image = models.ImageField(upload_to='photos/gallery')
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image_name = models.CharField(max_length=100, null=True)
    # video = models.
    # audio = models.

    def gallery_url(self):
        return reverse('gallery_detail', args=[self.id])

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.image_name
