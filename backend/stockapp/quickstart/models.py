from django.db import models

class Stock(models.Model):
    stock_name = models.CharField(max_length=50)
    change_percent = models.CharField(max_length=50)
    change_dollar = models.CharField(max_length=50)
    stock_price = models.CharField(max_length=50)
    