from django.db import models
from datetime import date

# Create your models here.
class Emission(models.Model):
    # id field ignored as django creates IDs automatically
    date_created = models.DateField(default=date.today)
    accounting_period = models.CharField(max_length=500)
    scope1 = models.IntegerField(null=True)
    scope2 = models.IntegerField(null=True)
    scope3 = models.IntegerField(null=True)