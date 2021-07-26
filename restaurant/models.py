from django.db import models
from FoodDelivery.models import UserDetails, City, Address
# Create your models here.

#===========================================Type of Restaurents===============================================================

class Rtype(models.Model):#type for restaurant
	rtype = models.CharField(max_length = 100)

#===========================================Restaurent================================================================

class Restaurants(models.Model):#Restaurent model to add restautant informations
	name = models.CharField(max_length = 200)#restaurent name
	details = models.CharField(max_length = 1500)#restaurent details
	rtype = models.ForeignKey(Rtype,on_delete = models.DO_NOTHING)#restaurent type which is reff by rtype
	image = models.ImageField(upload_to = 'Restaurant_images', blank=True)#restaurent image
	location = models.CharField(max_length = 500)#restaurent location
	city = models.ForeignKey(City, on_delete = models.DO_NOTHING)#restaurent city
	seats = models.IntegerField(default=50)
	since = models.CharField(max_length=100,default='1999')
	user = models.ForeignKey(UserDetails, on_delete = models.DO_NOTHING)#
	mobile = models.CharField(max_length=15,default='0000000000')

#====================================Restaurant Image==========================================================================

class RestImg(models.Model):
	resto = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING)
	img = models.ImageField(upload_to = 'Restaurant_images', blank=True)
 	
#===================================Restaurant Rating===========================================================================

class RestChefs(models.Model):
	resto = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING)
	name = models.CharField(max_length=200)
	post =models.CharField(max_length=200,default='')
	details = models.CharField(max_length=500,default='')
	img = models.ImageField(upload_to = 'Restaurant_images', blank=True)

#===========================================================================================================
class Rrating(models.Model):
	restaurant = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING) 
	rating = models.IntegerField()

#========================================= Food Category ==============================================================

class FoodCategory(models.Model):
	catname = models.CharField(max_length = 100)

#=============================== Food Type =====================================================================================

class FoodType(models.Model):
	ftype=models.CharField(max_length=200)

#=================================== Food ==============================================================================================

class Food(models.Model):
	name = models.CharField(max_length = 200)
	details = models.CharField(max_length = 500)
	fcategory = models.ForeignKey(FoodCategory, on_delete =  models.DO_NOTHING)
	ftype = models.ForeignKey(FoodType, on_delete =  models.DO_NOTHING,blank=True, default='')
	restaurant = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING)
	image = models.ImageField(upload_to = 'Food_images', blank=True)
	price = models.CharField(max_length = 100)

#====================================== Food reating ======================================================================

class FoodRating(models.Model):
	food = models.ForeignKey(Food,on_delete = models.DO_NOTHING ,default='1')
	rating = models.IntegerField()

#================================== Food Images ============================================================================

class FoodImage(models.Model):
	restaurant = models.ForeignKey(Restaurants, on_delete = models.DO_NOTHING)
	image = models.ImageField(upload_to = 'Food_images', blank=True)
	food= models.ForeignKey(Food,on_delete=models.DO_NOTHING,default=5)

#======================================= Restaurent Staff =======================================================================

class Staff(models.Model):
	name=models.CharField(max_length=100)
	salary=models.IntegerField()
	post=models.CharField(max_length=100)
	rest=models.ForeignKey(Restaurants,on_delete=models.DO_NOTHING)