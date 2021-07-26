from django.db import models
from FoodDelivery.models import UserDetails
from restaurant.models import *
from delivery.models import *

# Create your models here.

class Booking(models.Model):
	bookingid = models.CharField(max_length = 100)
	ordertime = models.DateTimeField(auto_now =True)
	delevirytime = models.CharField(max_length = 50)
	location = models.CharField(max_length = 200)
	status = models.IntegerField()
	qty = models.IntegerField(default=1)
	user = models.ForeignKey(UserDetails, on_delete = models.DO_NOTHING)
	rest = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING)
	delivboy = models.ForeignKey(Deliveryboy, on_delete = models.DO_NOTHING)
	food = models.ForeignKey(Food, on_delete = models.DO_NOTHING)


class Cart(models.Model):
	class Meta():
		unique_together=('user','food')
	user=models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
	food=models.ForeignKey(Food,on_delete=models.DO_NOTHING)

class Reservation(models.Model):
	user=models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
	rest=models.ForeignKey(Restaurants,on_delete=models.DO_NOTHING)
	prnum=models.IntegerField()
	time = models.CharField(max_length=100, default='00:00 PM')
	date= models.DateTimeField(auto_now=True)

class Caddress(models.Model):
	cname=models.CharField(max_length=100)
	caddress=models.CharField(max_length=1000)
	mobile=models.CharField(max_length=10, default='8435587742')
	user=models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)