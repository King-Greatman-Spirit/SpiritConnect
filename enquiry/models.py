from django.db import models

# Create your models here.
channel_chioce = (
    (0,'Select How you heard about us'),
    ('Facebook','Facebook'),
    ('Instagram', 'Instagram'),
    ('Twitter','Twitter'),
    ('Whatsapp','Whatsapp'),
    ('Google','Google'),
    ('word of mouth','Word of Mouth'),
    ('youtube','Youtube'),
    ('Ads','Ads'),
    ('others','Others'),
)


class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    job_title = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    channel = models.CharField(max_length=100, choices=channel_chioce, default=0)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
#
# class ContactForm(models.Model):
#     instruction = models.TextField(max_length=500, blank=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.instruction.
