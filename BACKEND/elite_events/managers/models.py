from django.db import models


class manager(models.Model):
	name = models.CharField(max_length =50)
	username= models.CharField(max_length = 50)
	password= models.CharField(max_length = 50)
	status= models.CharField(max_length =20,default="Active")
	email= models.CharField(max_length =50)
	address= models.CharField(max_length =200)
	dob= models.CharField(max_length =20)
	phone_no= models.CharField(max_length =20)
	organization= models.CharField(max_length =20,blank=True)
	experience= models.IntegerField(blank=True)
	previous_organization= models.CharField(max_length =20,blank=True)



