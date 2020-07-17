from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=100, null=False)
    plan = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    subcategory = models.CharField(max_length=100, null=True)
    primary_cancellation = models.URLField(max_length=1000, null=True)
    secondary_cancellation = models.EmailField(max_length=100, null=True)