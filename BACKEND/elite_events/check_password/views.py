from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from customers . models import customer
from managers . models import manager


def check_customer_password(request):
	if request.method=="POST":
		data=json.loads(request.body)
		password=data['password']
		id=data['id']

		print(data)
		try:
			
			if customer.objects.filter(id=id,password=password).exists():
				message="correct password"
			else:
				message="wrong password"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)


def check_manager_password(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['password']
		id=data['id']

		print(data)
		try:
			if manager.objects.filter(id=id,password=password).exists():
				message="correct password"
			else:
				message="wrong password"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)