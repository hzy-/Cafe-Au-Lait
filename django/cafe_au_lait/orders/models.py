from django.db import models
from beverages.models import Beverage

class Order(models.Model):
	date_time = models.DateTimeField(auto_now_add=True)
	tendered = models.IntegerField()
	current = models.BooleanField(default=True)

	def __unicode__(self):
		return self.date_time

class Content(models.Model):
	order = models.ForeignKey('Order')
	beverage = models.ForeignKey('beverages.Beverage')
	takeaway = models.BooleanField()
	quantity = models.IntegerField()

b = Beverage(name="cappicuno", price="3")
b.save()
b = Beverage(name="latte", price="3")
b.save()
b = Beverage(name="iced", price="3")
b.save()
b = Beverage(name="espresso", price="3")
b.save()
