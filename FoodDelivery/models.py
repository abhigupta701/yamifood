from django.db import models
from django.contrib.auth.models import User

#==========================================State==============================================================================

class State(models.Model):
	sname = models.CharField(max_length = 150)
	def __str__(self):
		return self.sname

#===========================================City========================================================================

class City(models.Model):
	cname = models.CharField(max_length = 150)
	state=models.ForeignKey(State,on_delete = models.DO_NOTHING)
	def __str__(self):
		return self.cname

#========================================UserDetails====================================================================

class UserDetails(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	role = models.CharField(max_length = 25)
	address = models.CharField(max_length = 200)
	img = models.ImageField(upload_to = "user_image",blank=True)
	mobile = models.CharField(max_length = 15)
	city = models.ForeignKey(City,on_delete = models.DO_NOTHING,default='1')

#=======================================User Address====================================================================

class Address(models.Model):
	add1 = models.CharField(max_length = 200)
	add2 = models.CharField(max_length = 200)
	landmark = models.CharField(max_length = 100)
	city = models.ForeignKey(City, on_delete = models.DO_NOTHING)
	mobile_n = models.CharField(max_length = 15)
	aadhar = models.CharField(max_length = 20)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
