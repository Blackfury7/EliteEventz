from django.db import models


class event(models.Model):
	name = models.CharField(max_length =100)
	status = models.CharField(max_length =50,default="Active")
	price = models.IntegerField()


class decoration(models.Model):
	name = models.CharField(max_length =100)
	status = models.CharField(max_length =20,default="Active")
	price = models.IntegerField()
	# phone_no = models.CharField(max_length =20)
	# email = models.CharField(max_length =100)
	# address = models.CharField(max_length =100)
	# organization = models.CharField(max_length =100)


class venues(models.Model):
	name = models.CharField(max_length =100)
	status = models.CharField(max_length =20,default="Active")
	price = models.IntegerField()
	# phone_no = models.CharField(max_length =20)
	# email = models.CharField(max_length =100)
	# address = models.CharField(max_length =100)
	# organization = models.CharField(max_length =100)


class photography(models.Model):
	name = models.CharField(max_length =100)
	status = models.CharField(max_length =20,default="Active")
	price = models.IntegerField()
	# phone_no = models.CharField(max_length =20)
	# email = models.CharField(max_length =100)
	# address = models.CharField(max_length =100)
	# organization = models.CharField(max_length =100)