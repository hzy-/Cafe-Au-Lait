#misc tools
from django.shortcuts import render_to_response
from django.core.cache import cache

#models
from orders.models import Order, Content
from beverages.models import Beverage

def list(request):
	if cache.get('beverages_list_b'):
		b = cache.get('beverages_list_b')
	else:
		b = Beverage.objects.all()
		cache.set('beverage_list_b', b)
	return render_to_response('beverages/list.html', {"beverages": b})
