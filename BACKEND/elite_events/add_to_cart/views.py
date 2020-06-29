from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book
from events . models import event, venues, decoration, photography

def add_to_cart(request):
	if request.method=="POST":
		data=json.loads(request.body)
		customer_id=data['id']
		print(data)

		event_id=data['event_id']
		venues_id=data['venues_id']
		deco_id=data['decoration_id']
		photo_id=data['photography_id']

		try:
			amount = event.objects.get(id=event_id).price + venues.objects.get(id=venues_id).price + decoration.objects.get(id=deco_id).price + photography.objects.get(id=photo_id).values
			
			book.objects.create(**data, payment=amount)
			message='Added to cart'
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)