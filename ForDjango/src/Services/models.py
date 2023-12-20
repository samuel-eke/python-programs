from django.db import models

# Create your models here.

class Services(models.Model):
    Service_provider = models.CharField(max_length=30)
    service_description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    location = models.TextField(default="Abuja")
    featured = models.BooleanField(default=False)