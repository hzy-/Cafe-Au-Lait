from django.db import models
from beverages.models import Beverage

class Order(models.Model):
	date_time = models.TimeField(auto_now_add=True)
	tendered = models.IntegerField()

	def __unicode__(self):
		return self.date_time

class Content(models.Model):
	order = models.ForeignKey('Order')
	beverage = models.ForeignKey('beverages.Beverage')
	takeaway = models.BooleanField()
	quantity = models.IntegerField()
