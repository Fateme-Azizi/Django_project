from django.db import models

# Create your models here.


class DimCompany(models.Model):
    id = models.IntegerField()
    symbol = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    state = models.IntegerField()


class FactStatement(models.Model):
    id = models.IntegerField()
    item_id = models.IntegerField()
    item_value = models.IntegerField()
    unit = models.CharField(255)
    company_id = models.ForeignKey(DimCompany, on_delete=models.CASCADE)
    period = models.IntegerField()
    period_end_to_date = models.CharField(255)
