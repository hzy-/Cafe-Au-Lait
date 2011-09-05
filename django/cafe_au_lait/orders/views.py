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
	message = 'Something went wrong :('
	if request.is_ajax():
		if request.method == 'POST':
			# Here we can access the POST data
			itemlist = simplejson.loads(request.raw_post_data)
			o = None
			#loops through the provided json
			for item in itemlist:
				if item['value']:
					if int(item['value']) > 0:
						#checks if the order exists yet
						if o == None:
							o = Order(tendered="1000", table="1")
							o.save()
						c = Content(order= o, quantity= item['value'])
						#determines the type of the drink
						if str(item['name'])[:1] == "d":
							c.takeaway = False
						elif str(item['name'])[:1] == "t":
							c.takeaway = True
						c.beverage = Beverage.objects.get(pk= str(item['name'])[2::])
						c.save()
			cache.delete_many(['orders_current_orders', 'orders_current_contents'])
			message = "XHR Complete"
	return HttpResponse(message)

def current(request):
	error = True
	if request.is_ajax():
		if request.method == 'GET':
			error = False
			#checks cache for current &content items, if they're there it gets it from the cache, 
			#otherwise it runs the sql and then saves the result to the cache.
			if cache.get('orders_current_orders') and cache.get('orders_current_contents'):
				x = cache.get_many(['orders_current_orders', 'orders_current_contents'])
				orders = x['orders_current_orders']
				contents = x['orders_current_contents']
			else:
				orders = Order.objects.filter(current=True)
				contents = Content.objects.filter(order__current=True)
				cache.set('orders_current_orders', orders)
				cache.set('orders_current_contents', contents)
			return render_to_response('orders/current.html', {"orders": orders, "contents": contents})
	if (error == True):
		return HttpResponse('Something went wrong :(')

def clear(request):
	if request.is_ajax():
		if request.method == 'POST':
			if request.POST['order']:
				order = Order.objects.get(pk=int(request.POST['order']))
				order.current = False
				order.save()
				cache.delete_many(['orders_current_orders', 'orders_current_contents'])
				return HttpResponse('yay')
