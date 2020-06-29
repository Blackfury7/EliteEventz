from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from customers . models import customer
from managers . models import manager


def customer_signup(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		email=data['email']
		phone_no=data['phone_no']
		print(data)
		try:
			
			if customer.objects.filter(username=username).exists():
			    message='This username is already taken'
			 
			elif customer.objects.filter(email=email).exists():
			 
			    message='This email is already registered'
			elif customer.objects.filter(phone_no=phone_no).exists():
			 
			    message='This phone is already registered'
			
			else:
			
				customer.objects.create(**data)
			

				message="You are successfully registered"

		except: 
			message="Error: Could not process your request"
		
		return JsonResponse(message,safe=False)

def manager_signup(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		email=data['email']
		phone_no=data['phone_no']
		print(data)
		try:
			
			if manager.objects.filter(username=username).exists():
			    message='This username is already taken'
			 
			elif manager.objects.filter(email=email).exists():
			 
			    message='This email is already registered'
			elif manager.objects.filter(phone_no=phone_no).exists():
			 
			    message='This phone is already registered'
			
			else:
			
				manager.objects.create(**data)
			

				message="You are successfully registered"

		except: 
			message="Error: Could not process your request"
		
		return JsonResponse(message,safe=False)







		