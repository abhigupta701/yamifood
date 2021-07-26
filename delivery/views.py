from django.shortcuts import render, redirect
from customer.models import *
from FoodDelivery.models import *
from .models import *

# Create your views here.
#================================================= Delivery Home ==================================================================

def home(request):
	
		user=UserDetails.objects.get(user = request.user)
		deliv=Drating.objects.filter(boy__user=user)
		d=Deliveryboy.objects.get(user=user)
		bok=Booking.objects.filter(delivboy=d)
		book=0
		for i in bok:
			book+=1
		total=0
		counter=0
		for i in deliv:
			counter+=1
			total+=i.rating
		if counter==0:
			rating=0
		else:
			rating=total/counter
			rating=str(rating)[:3]

		if str(user.role) == 'delivery':
			a=1
			if str(request.user) == "AnonymousUser":
				a = 0
			return render(request,'delivery/delivery.html',{'not':a,'rating':rating,'book':book})
		else:
			return redirect('/')
	

#================================================= Order ==============================================================================

def order(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'delivery':
			user=Deliveryboy.objects.get(user__user__username=request.user)
			book=Booking.objects.filter(delivboy=user)
			return render(request,'delivery/deli.html',{'book':book})
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================== Status ====================================================================================

def status(request,id):
	try:
		book=Booking.objects.get(id=id)
		b=book.status+1
		booking=Booking.objects.filter(id=id)
		booking.update(status=b)
		return redirect('/delivery/order/')
	except:
		return redirect('/delivery/')

#=================================================== History ======================================================================================

def history(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'delivery':
			user=Deliveryboy.objects.get(user__user__username=request.user)
			book=Booking.objects.filter(delivboy=user)
			return render(request,'delivery/history.html',{'book':book})
		else:
			return redirect('/')
	except:
		return redirect('/')

#==================================================================================================================================================