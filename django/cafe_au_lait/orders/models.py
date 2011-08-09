from django.db import models

class Order(models.Model):
	json = models.TextField()
	date_time = models.TimeField(auto_now_add=True)
	def __unicode__(self):
		return self.json
