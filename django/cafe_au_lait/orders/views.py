from django.http import HttpResponse
from orders.models import Order
from django.utils import simplejson

def submit(request):
	if request.is_ajax():
		if request.method == 'GET':
			message = "This is an XHR GET request"
		elif request.method == 'POST':
			message = "This is an XHR POST request"
			# Here we can access the POST data
			#print request.POST
			arr = simplejson.loads(request.raw_post_data)
			o = Order(json = arr)
			o.save()
			message = arr
	else:
		message = "No XHR"
	return HttpResponse(message)
