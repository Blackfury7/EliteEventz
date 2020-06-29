from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from customers . models import customer
from managers . models import manager


def customer_login(request):
	if request.method == "POST":
		data=json.loads(request.body)
		username=data['username']
		password=data['password']
		user=customer.objects.filter(username=username,password=password)
		if user.exist():
			message = user['id']
		else:
			message="Invalid details"
		return JsonResponse(message,safe=False)

def manager_login(request):
	if request.method =="POST":
		data=json.loads(request.body)
		username=data['username']
		password=data['password']
		MANAGER=manager.objects.filter(username=username,password=password)
		if MANAGER.exist():
			message = MANAGER['id']
		else:
			message="Invalid details"
		return JsonResponse(message,safe=False)
	


















