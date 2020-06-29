from django.db import models

from events . models import event,decoration,venues,photography
from customers . models import customer

class book(models.Model):
	customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
	event=models.ForeignKey(event,null=True,on_delete=models.SET_NULL)
	decoration=models.ForeignKey(decoration,null=True,on_delete=models.SET_NULL)
	venues=models.ForeignKey(venues,null=True,on_delete=models.SET_NULL)
	photography=models.ForeignKey(photography,null=True,on_delete=models.SET_NULL)
	status = models.CharField(max_length =50,default="None")
	add_status = models.CharField(max_length =50,default="Added")
	payment = models.IntegerField(blank=True)
	payment_status = models.CharField(max_length =50,default="Pending")
	people = models.IntegerField(blank=True)
	no_of_days = models.IntegerField(blank=True)
	date = models.CharField(max_length =50,blank=True)
	time = models.CharField(max_length =50,blank=True)
	is_date_changed = models.CharField(max_length =50,blank=True)
	reason_of_rejection = models.CharField(max_length =300,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)