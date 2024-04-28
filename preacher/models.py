from django.db import models

# Create your models here.
class Preacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='photos/preachers')
    gender = (
        (0, 'Select Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
    )
    is_worker = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    created_date    = models.DateTimeField(blank=True, null=True)




    class Meta:
        verbose_name = 'preacher'
        verbose_name_plural = 'preachers'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
