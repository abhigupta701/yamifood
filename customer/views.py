from django.shortcuts import render,redirect
from restaurant.models import *
from FoodDelivery.models import *
from customer.models import *
import datetime
import time
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#Create your views here.
# messages.success(request, "food Added")
# messages.error(request, "Already in Cart")

#========================================= Count ============================================================================================

def Count(request):
	if str(request.user) == "AnonymousUser":
		count=0
	else:
		user=UserDetails.objects.get(user__username=request.user)
		count=Cart.objects.filter(user=user).count()
	return count

#========================================  =================================================================================================
def search(request):
	count=Count(request)
	search=request.POST['search']
	data=Food.objects.all()
	food=[]
	print(food)
	for i in data:
		i1=i.name.lower()
		search=search.lower()
		if search in i1:
			food.append(i)
	return render(request,'customer/search.html',{'food':food,'count':count})

#============================================== Customer Home ===========================================================================================
def home(request):
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	count=Count(request)
	book=Food.objects.all()
	counts=0
	books=[]
	for i in book:
		counts+=1
		if counts <4:
			books.append(i)
	return render(request,'customer/home.html',{'not':a,'count':count,'food':books})

#=================================================== Resturant ================================================================================================

def rest(request,id):
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	rest=Restaurants.objects.get(id=id)
	food=Food.objects.filter(restaurant=rest)
	chef = RestChefs.objects.filter(resto=rest)
	imgs=RestImg.objects.filter(resto=rest)
	count=Count(request)
	return render(request,'customer/index.html',{'data':rest,'not':a,'food':food,'chef':chef,'imgs':imgs,'count':count})

#==================================================== Menu ==============================================================================================================

def menu(request):
	try:
		count=Count(request)
		s=State.objects.all()
		c=City.objects.all()
		cat=FoodCategory.objects.all()
		if str(request.user)!='AnonymousUser':
			user=UserDetails.objects.get(user__username=request.user)
			food=Food.objects.filter(restaurant__city=user.city)
		else:
			food=Food.objects.all()
		a=1
		if str(request.user) == "AnonymousUser":
			a = 0
		if request.method=='POST':
			u=UserDetails.objects.get(user__username=request.user)
			st=request.POST['st']
			cty=request.POST['cty']
			ct = request.POST['ct']
			if st!='State':
				food=Food.objects.filter(restaurant__city__state__id=st)
			if cty!='City':
				food=Food.objects.filter(restaurant__city__id=cty)
			if ct!='Category':
				food=Food.objects.filter(fcategory__id = ct)	
			return render(request,'customer/menu.html',{'not':a,'state':s,'city':c,'food':food,'cat':cat,'count':count})
		return render(request,'customer/menu.html',{'not':a,'state':s,'city':c,'food':food,'cat':cat,'count':count})
	except:
		return redirect('/login/')

#-------------------------------------------------restaurant-------------------------------------------------------------------

def restro(request):
	count=0
	state=State.objects.all()
	city=City.objects.all()
	cat=Rtype.objects.all()
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
		rest=Restaurants.objects.all()
	else:
		rest=Restaurants.objects.filter(user__user__is_staff=1)
		count=Count(request)
	if request.method=='POST':
		st=request.POST['st']
		cty=request.POST['cty']
		ct = request.POST['ct']
		if st!='State':
			rest=Restaurants.objects.filter(city__state__id=st)
		if cty!='City':
			rest=Restaurants.objects.filter(city__id=cty)
		if ct!='Category':
			rest=Restaurants.objects.filter(rtype__id = ct)	
		return render(request,'customer/restro.html',{'not':a,'data':rest,'state':state,'city':city,'cat':cat,'count':count})
	return render(request,'customer/restro.html',{'not':a,'data':rest,'state':state,'city':city,'cat':cat,'count':count})

#========================================== Contact =================================================================================================

def contact(request):
	#try:
		x=0
		u=UserDetails.objects.get(user__username=request.user)
		addr=Caddress.objects.filter(user=u)
		time1 = time.time() + 1800
		now=datetime.datetime.now()
		time2=now.strftime("%H:%M:%S")
		dtime=str(time.ctime(time1)).split()[3]
		count=Count(request)
		cart=Cart.objects.filter(user__user__username=request.user)
		user=UserDetails.objects.get(user__username=request.user)
		duser=Deliveryboy.objects.all()
		deliveryuser=[]
		for i in duser:
			if i.id==4:
				pass
			else:
				deliveryuser.append(i)
				
		re=random.choice(deliveryuser)
		if request.method=='POST':
			x=1
			qty=request.POST.getlist('num')
			add=request.POST['add']
			add1=Caddress.objects.get(id=add)
			oid=datetime.datetime.today()#date object
			x = str(oid).replace("-","").replace(' ','').replace(':','').replace('.','')#Creating Order ID
			total=0
			for i in range(len(cart)):
				rest=cart[i]
				fo=cart[i]

				book=Booking(bookingid=x,qty=qty[i],location=add1.caddress,ordertime=time2,delevirytime=dtime,status=0,user=user,rest=rest.food.restaurant,delivboy=re,food=fo.food)
				book.save()
				print(fo)
				c=Cart.objects.get(food=fo.food)
				c.delete()
				total+=int(fo.food.price)*int(qty[i])
			return render(request,'customer/contact.html',{'count':count,'x':x,'bill':total})
		return render(request,'customer/contact.html',{'count':count,'cart':cart,'add':addr,'x':x})
	#except Exception as e:
		#print(e)
		return redirect('/login/')

#======================================================== Delete Item =======================================================================================================

def delitem(request,id):
	c=Cart.objects.get(id=id)
	c.delete()
	return redirect('/customer/cart/')

#======================================================== Item ========================================================================================================

def item(request,id):
	try:
		count=Count(request)
		f=Food.objects.get(id=id)
		food=Food.objects.filter(restaurant=f.restaurant)
		img=FoodImage.objects.filter(food=f)
		return render(request,'customer/item.html',{'item':f,'food':food,'img':img,'count':count})
	except:
		pass

#======================================================= Booking =======================================================================================================

def booking(request,id):
	try:
		u=UserDetails.objects.get(user__username=request.user)
		count=Count(request)
		return render(request,'customer/booking.html',{'count':count})
	except:
		return redirect('/login/')

#======================================================= Cart ===============================================================================================================

@login_required(login_url='/login/')
def cart(request,id):
	try:
		food=Food.objects.get(id=id)
		user=UserDetails.objects.get(user__username=request.user)
		cart=Cart(food=food,user=user)
		cart.save()
		item(request,id)
		rest=Restaurants.objects.get(id=food.restaurant.id)
		messages.success(request, "food Added")
		return redirect('/cart/')
	except:
		messages.error(request, "Already in Cart")
		return redirect('/cart/')

#===================================================== Cartr =====================================================================================================

def cartr(request,id):
	food=Food.objects.get(id=id)
	user=UserDetails.objects.get(user__username=request.user)
	cart=Cart(food=food,user=user)
	cart.save()
	return redirect('/customer/restaurants/')

#======================================================= reserv ===============================================================================

def reserv(request,id):
	try:
		res=Restaurants.objects.get(id=id)
		user=UserDetails.objects.get(user__username=request.user)
		if request.method=='POST':
			num=request.POST['num']
			time=request.POST['time']
			rese=Reservation(user=user,prnum=num,rest=res,time=time)
			rese.save()
			return redirect('/customer/restaurants/')
		return render(request,'customer/reserv.html')
	except:
		return redirect('/login/')

#===================================================== Profile ===================================================================================

def profile(request):
	book=Booking.objects.filter(user__user__username=request.user)
	order=[]
	for i in book:
		if i.status < 3:
			order.append(i)
	user=UserDetails.objects.get(user__username=request.user)
	ad=Caddress.objects.filter(user=user)
	if request.method=='POST':
		name=request.POST['name']
		add=request.POST['add']
		num = request.POST['num']
		add1=add.replace('<iframe src="','').replace('" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',"")
		addr=Caddress(cname=name,caddress=add1,user=user,mobile=num)
		addr.save()
		return redirect('/customer/profile/')
	return render(request,'customer/profile.html',{'book':book,'add':ad,'order':order})

#=========================================================================================================================================================================
 
def urating(request):
	rr=request.POST['rr']
	dr=request.POST['dr']
	div=request.POST['div']
	rest=request.POST['rest']
	user=UserDetails.objects.get(user__username=request.user)#current user
	duser=UserDetails.objects.get(id=div)#deliveryboy User
	res = Restaurants.objects.get(id=rest)#restaurent
	deli=Deliveryboy.objects.get(user=duser)
	d=Drating(user=user,rating=dr,boy=deli)
	d.save()
	r=Rrating(restaurant=res,rating=rr)
	r.save()
	return redirect('/profile/')

#========================================================== order Cancel ===========================================================

def ocancel(request,id):
	b=Booking.objects.filter(id=id)
	b.delete()
	return redirect('/customer/profile/')

#==========================================================================================================================================================