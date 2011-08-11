#various tools / utilities / functions
from django.http import HttpResponse
from django.utils import simplejson
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.core.cache import cache

#models
from orders.models import Order, Content
from beverages.models import Beverage

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
			cache.delete_many(['orders_current_current', 'orders_current_content'])
			message = "XHR Complete"

	else:
		message = "No XHR"
	return HttpResponse(message)

def current(request):
	#checks cache for current (&content) items, if it's there it gets it from the cache, 
	#otherwise it runs the sql and then saves the result to the cache.
	if cache.get('orders_current_current'):
		current = cache.get('orders_current_current')
	else:
		current = Order.objects.filter(current=True)
		cache.set('orders_current_current', current)
	
	if cache.get('orders_current_content'):
		content = cache.get('orders_current_content')
	else:
		content = Content.objects.filter(order__current=True)
		cache.set('orders_current_content', content)
	return render_to_response('current.html', {"currentitems": current, "contents": content})
