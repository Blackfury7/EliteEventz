from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from booking . models import book


def customer_payment_history(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		payments=book.objects.filter(customer_id=id,payment_status="Paid").values('id','event__name','venues__name','payment','status','date','timestamp')
		return JsonResponse(payments,safe=False)

def payment_history_list(request):
	if request.method=="GET":
		payments=book.objects.filter(payment_status="Paid").values('id','customer_id','customer_name','event__name','venues__name','payment','status','date','timestamp')
		return JsonResponse(payments,safe=False)