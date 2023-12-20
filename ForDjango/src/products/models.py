from django.db import models
# Create your models here.

#this gets save to the database side of our project. containing information about our product
class Proudcts(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(default='This is an example of a default text', blank=True)
    featured = models.BooleanField(default=False)



