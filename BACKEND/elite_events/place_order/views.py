from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book

def confirm_order(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		#data
		#status=Pending ,add_status="Done",payment_status="Paid" 
		try:
			book.objects.filter(id=id).update(**data,status="Pending")
			message="Your order is placed. We will soon give you update"
		except:
			message="Error: your request could not be processed"

		return JsonResponse(message,safe=False)

def remove_order(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		 
		try:
			book.objects.filter(id=id).delete()
			message="Item is removed"
		except:
			items="Error: your request could not be processed"

		return JsonResponse(message,safe=False)