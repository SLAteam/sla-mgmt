from django.db import models
from django.contrib.auth.models import User

class Operator(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class AggregationType(models.Model):
    kpi_type = models.CharField(max_length=30)

    def __str__(self):
        return self.kpi_type


class KeyPerformanceIndicator(models.Model):
    name = models.CharField(max_length=128)
    aggregation_type = models.ForeignKey(AggregationType, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    customer = models.CharField(max_length=50) # TODO: Change to Customer model
    value = models.DecimalField(max_digits=20, decimal_places=10)
    country = models.CharField(max_length=30, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    kpi_count = models.BigIntegerField(null=True, blank=True)
    symbol = models.CharField(max_length=50, null=True, blank=True)



    def __str__(self):
        return self.name
