from django.db import models

class Operator(models.Model):
    name = models.CharField(max_length=128)

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
    value = models.DecimalField(max_digits=20, decimal_places=10)
    country = models.CharField(max_length=30)
    comment = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name
