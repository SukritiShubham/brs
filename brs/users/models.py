from django.db import models

# Create your models here.
from django.db import models


class user(models.Model):
    company = models.TextField()
    quarter = models.CharField(max_length=10)
    profit = models.DecimalField(max_digits=18, decimal_places=2)
    expected = models.DecimalField(max_digits=18, decimal_places=2)
    submitted = models.BooleanField()