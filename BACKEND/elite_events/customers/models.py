from django.db import models


class customer(models.Model):

	
	name = models.CharField(max_length =50)
	username= models.CharField(max_length = 50)
	password= models.CharField(max_length = 50)
	status= models.CharField(max_length =20,default="Active")
	phone_no= models.CharField(max_length =20)
	email= models.CharField(max_length =50)
	address= models.CharField(max_length =200,blank=True)
	dob= models.CharField(max_length =20,blank=True)
	


