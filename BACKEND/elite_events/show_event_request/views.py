from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book

def customer_event_request(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		try:
			items=book.objects.filter(customer_id=id,status="Pending",add_status="Done").values('id','venues__name',
				'venues__price','event__name','event__price','decoration_name','decoration__price',
				'photography__name','photograpy__price','status','payment_status','payment','date','time','person','days')
		except:
			items="Error: your request could not be processed"
		return JsonResponse(items,safe=False)

def event_request_list(request):
	if request.method=="GET":
		try:
			items=book.objects.filter(customer_id=id,status="Pending",add_status="Done").values('id','venues__name',
				'venues__price','event__name','event__price','decoration_name','decoration__price',
				'photography__name','photograpy__price','status','payment_status','payment','date','time','person','days')
		except:
			items="Error: your request could not be processed"
		return JsonResponse(items,safe=False)