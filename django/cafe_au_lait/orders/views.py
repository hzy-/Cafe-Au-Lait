from django.http import HttpResponse
from orders.models import Order, Content
from beverages.models import Beverage
from django.utils import simplejson

def submit(request):
	if request.is_ajax():

		if request.method == 'GET':
			message = "This is an XHR GET request"

		elif request.method == 'POST':
			# Here we can access the POST data
			itemlist = simplejson.loads(request.raw_post_data)
			o = Order(tendered="1000")
			o.save()
			#loops through the provided json
			for item in itemlist:
				if item['value']:
					if int(item['value']) > 0:
						c = Content(order= o, quantity= item['value'])
						#determines the type of the drink
						if str(item['name'])[:1] == "d":
							c.takeaway = False
						elif str(item['name'])[:1] == "t":
							c.takeaway = True
						c.beverage = Beverage.objects.get(name= str(item['name'])[2::])
						c.save()
			message = "XHR Complete"

	else:
		message = "No XHR"
	return HttpResponse(message)
