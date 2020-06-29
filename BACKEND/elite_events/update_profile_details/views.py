from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from customers . models import customer
from managers . models import manager


def update_customer_profile(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		try:
			customer.objects.filter(id=id).update(**data)
			message="Your profile is updated"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)


def update_manager_profile(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		try:
			manager.objects.filter(id=id).update(**data)
			message="Your profile is updated"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)