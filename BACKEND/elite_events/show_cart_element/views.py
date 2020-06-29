from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book

def show_cart_element(request):
	if request.method=="POST":
		data=json.loads(request.body)
		customer_id=data['id']
		print(data)
		try:
			items=list(book.objects.filter(customer_id=customer_id,add_status="Added").values('id','venues__name','venues__price',
				'event__name','event__price','decoration_name','decoration__price','photography__name',
				'photograpy__price','payment','date','time','person','days'))
		except:
			items="Error: your request could not be processed"

		return JsonResponse(items,safe=False)