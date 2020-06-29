from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from customers . models import customer
from managers . models import manager


def check_customer_username(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		id=data['id']

		print(data)
		try:
			
			if customer.objects.filter(username=username).exists():
			    message='This username is already taken'
			else:
				
				message="Unique username"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)


def check_manager_username(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		id=data['id']

		print(data)
		try:
			
			if manager.objects.filter(username=username).exists():
			    message='This username is already taken'
			else:
				
				message="Unique username"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)