from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book
from django.db.models import Q



def customer_booked_event(request):
	if request.method=="POST":
		data=json.loads(request.body)
		customer_id=data['id']
		print(data)
		booked_events=book.objects.filter(Q(status="Active")|Q(status="Done"),customer_id=customer_id).values('id','event__name',
			'venues__name','payment','status','date','timestamp')
		return JsonResponse(booked_events,safe=False)

def booked_event_list(request):
	if request.method=="GET":
		booked_events=book.objects.filter(Q(status="Active")|Q(status="Done")).values('id','event__name','customer_id',
			'customer__name','venues__name','payment','status','date','timestamp')
		return JsonResponse(booked_events,safe=False)