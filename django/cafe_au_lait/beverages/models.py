from django.db import models

class Beverage(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()
