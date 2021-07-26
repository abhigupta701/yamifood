from django.db import models
from FoodDelivery.models import UserDetails

# Create your models here.
#=========================================rating for delivery boy==================================================

class Deliveryboy(models.Model):
	user = models.ForeignKey(UserDetails,on_delete = models.DO_NOTHING)
	rating = models.IntegerField()

#==============================================chating with delivery boy=================================================

class Chat(models.Model):
	boy = models.ForeignKey(Deliveryboy, on_delete = models.DO_NOTHING)
	chat = models.CharField(max_length = 200)
	user = models.ForeignKey(UserDetails, on_delete = models.DO_NOTHING)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++ Delivery Boy Rating ++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Drating(models.Model):
	user=models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
	rating=models.IntegerField()
	boy=models.ForeignKey(Deliveryboy,on_delete=models.DO_NOTHING)