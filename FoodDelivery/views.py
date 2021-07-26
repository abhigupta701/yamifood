from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from restaurant.models import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from customer.models import *
import random
from delivery.models import *

#===================================================home=============================================================================================

def home(request):
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	return render(request,'index.html',{'not':a})

#===================================================Signin========================================================================================

def signin(request):
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	if request.method=="POST":
		un=request.POST['un']#user name
		pw=request.POST['pw']#password
		au=authenticate(username=un,password=pw)#authenticating user is valid or not
		if au:
			login(request,au)#creating login session
			use=UserDetails.objects.get(user__username=request.user)#retriving user object
			if use.role=='restaurant':#
				if use.user.is_staff==1:
					return redirect('/restaurant/')
				else:
					return render(request,'response.html')
			elif use.role=='admin':#
				return redirect('/adminstuff/')

			elif use.role=='user':#
				return redirect('/customer/')

			elif use.role == 'delivery':
				if use.user.is_staff==1:
					return redirect('/delivery/')
				else:
					return render(request,'response.html')
			else:
				return HttpResponse('<h1>UserType None</h1>')#if user is not blongs from any type
		else:
			return HttpResponse('<a href="/login/" style="color: red; font-size: 20px">Invalid User Please Click Here For Login</a>')#if user is not  valid is show 
	return render(request,'login.html',{'not':a})


#===================================================Signup=====================================================================================================

def signup(request):
	rtype=Rtype.objects.all()
	city=City.objects.all()
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	return render(request,'signup.html',{'not':a,'data':city,'type':rtype})

#=====================================================loguot==========================================================================================================

def logout_call(request):
	logout(request)#logout request
	return redirect('/login/')

#================================================== customer adding ==================================================================================================

def useradd(request):
	fn=request.POST['fn']#firsh name
	ln=request.POST['ln']#last name
	un=request.POST['un']#username
	pw=request.POST['pw']#password
	eml=request.POST['eml']#
	ph=request.POST['pn']#phone number
	ad=request.POST['ad']#addressemail
	img=request.FILES['img']
	ad=ad.replace('<iframe src="','').replace('" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',"")
	user=User(first_name=fn,last_name=ln,username=un,password=make_password(pw),email=eml)
	user.save()
	u=UserDetails(user=user,role='user',address=ad,img=img,mobile=ph)
	u.save()
	return redirect('/login/')

#==========================================delivery user adding==================================================================

def add_deli(request):
	fn=request.POST['fn']#firsh name
	ln=request.POST['ln']#last name
	un=request.POST['un']#username
	pw=request.POST['pw']#password
	eml=request.POST['eml']#Email
	ph=request.POST['pn']#phone number
	ad=request.POST['ad']#address
	img=request.FILES['img']#image
	aadhar=request.POST['aad']#aadhar Number
	city1=request.POST['city']#city id
	ci=City.objects.get(id=city1)#City Object
	ad=ad.replace('<iframe src="','').replace('" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',"")
	user=User(first_name=fn,last_name=ln,username=un,password=make_password(pw),email=eml)
	user.save()
	ad1=Address(aadhar=aadhar,city=ci,user=user)
	ad1.save()
	u=UserDetails(user=user,role='delivery',address=ad,img=img,mobile=ph)
	u.save()
	d=Deliveryboy(user=u,rating=0)
	d.save()
	return redirect('/login/')

#==========================================resturent user adding==================================================================

	#------------------------------------------user details---------------------------------------------------------
def addrest(request):
	fn=request.POST['fn']#firsh name
	ln=request.POST['ln']#last name
	un=request.POST['un']#username
	pw=request.POST['pw']#password
	eml=request.POST['eml']#
	ph=request.POST['pn']#phone number
	img=request.FILES['img']
	ad=request.POST['ad']#addressemail

	#--------------------------------------restro details---------------------------------------------------------------
	
	hnm = request.POST['hnm']#Restaurent name
	details = request.POST['dtl']#details
	htype1 = request.POST['ty']#Resturent type
	location = request.POST['loct']#restaurent location
	city1 = request.POST['city']#restaurent city
	himg = request.FILES['himg']#images
	city = City.objects.get(id=city1)
	htype = Rtype.objects.get(id=htype1)
	since=request.POST['since']
	mobile1=request.POST['mobile1']
	loc=location.replace('<iframe src="','').replace('" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',"")
	user = User(first_name=fn,last_name=ln,username=un,password=make_password(pw),email=eml)
	user.save()
	u=UserDetails(user=user,role='restaurant',address=ad,img=img,mobile=ph)
	u.save()
	r=Restaurants(name=hnm,details=details,rtype=htype,location=loc,image=himg, city=city,user=u,since=since,mobile=mobile1)
	r.save()
	return redirect('/login/')

#-------------------------------------------------Admin------------------------------------------------------------------------

def admins(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			a=1
			if str(request.user) == "AnonymousUser":
				a = 0
			b=Booking.objects.all()
			count=len(b)

			return render(request,'admin.html',{'not':a,'counter':count})
		else:
			return redirect('/')
	except Exception as e:
		print(e)

		return redirect('/')


#=======================================================Add State==============================================================

def state(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			st=request.POST['st']
			state=State(sname=st)
			state.save()
			return redirect('/addaddr/')
	except:
		return redirect('/')

#========================================================= City ==========================================================================

def city(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			ct=request.POST['ct']
			st=request.POST['st']
			state=State.objects.get(id=st)
			city=City(cname=ct,state=state)
			city.save()
			return redirect('/addaddr/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#====================================================== Add Address ======================================================================

def addadder(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			st=State.objects.all()
			a=1
			if str(request.user) == "AnonymousUser":
				a = 0
			return render(request,'addcity.html',{'not':a,'state':st})
		else:
			return redirect('/')
	except:
		return redirect('/')

#=================================================== Verify Delivery =======================================================================

def verifyd(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			deliv=UserDetails.objects.filter(role='delivery')
			delive=[]
			for i in deliv:
				if i.user.is_staff == 0:
					delive.append(i)
			if request.method == 'POST':
				rid=request.POST['rid']
				email=request.POST['email']
				subject = 'Thank you for registering to  Yami Food Delivery'
				message = 'Hello \nYou registered an account on Yami Food Delivery, \nbefore being able to use your account you need to verify that this is your email address \nby clicking : '+' http://localhost:8000/verifys/'+str(rid)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [email,]
				send_mail( subject, message, email_from, recipient_list )
				return redirect('/verifydelivery/')
			return render(request,'verify.html',{'data':delive})
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================== verify Restaurant ==================================================================================

def verifyr(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			rest=UserDetails.objects.filter(role='restaurant')
			resta=[]
			for i in rest:
				if i.user.is_staff==0:
					resta.append(i)
			if request.method=='POST':
				rid=request.POST['rid']
				email=request.POST['email']
				subject = 'Thank you for registering to  Yami Food Delivery'
				message = 'Hello \nYou registered an account on Yami Food Delivery, \nbefore being able to use your account you need to verify that this is your email address \nby clicking : '+' http://localhost:8000/verifys/'+str(rid)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [email,]
				send_mail( subject, message, email_from, recipient_list )
				return redirect('/verifyr/')
			return render(request,'verify.html',{'data':resta})
		else:
			return redirect('/')
	except Exception as e:
		print(e)
		return redirect('/')

#========================================================================================================================================

def verifys(request,id):

	user=User.objects.filter(id=id)
	user.update(is_staff=1)
	return redirect('/login/')
	
#============================================================================================================================================

def usermanage(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			rest=UserDetails.objects.filter(role='restaurant')
			deli=UserDetails.objects.filter(role='delivery')
			cust=UserDetails.objects.filter(role='user')
			return render(request,'usermanage.html',{"rest":rest,'deli':deli,'cust':cust})
		else:
			return redirect('/')
	except Exception as e:
		print(e)

		return redirect('/')

#==================================================================================================================================================

def userremove(request,id):
	user=UserDetails.objects.get(id=id)
	if user.role=='delivery':
		div=Deliveryboy.objects.get(user=user)
		d=Drating.objects.filter(boy=div)
		for i in d:
			de=Drating.objects.get(id=i.id)
			de.delete()
		div.delete()
	

	us=user.user.id
	user.delete()
	user1=User.objects.get(id=us)
	user1.delete()
	return redirect('/usermanage/')

#==========================================================================================================================================================

def userupdate(request,id):
	user=UserDetails.objects.get(id=id)
	us=User.objects.get(id=user.user.id)
	if request.method=='POST':
		fn=request.POST['fn']
		ln=request.POST['ln']
		eml=request.POST['eml']
		pwd=request.POST['pwd']
		role=request.POST['role']
		add=request.POST['add']
		mn=request.POST['mn']
		use=User.objects.filter(id=user.user.id)
		use.update(first_name=fn,last_name=ln,email=eml,password=make_password(pwd))
		used=UserDetails.objects.filter(id=id)
		used.update(role=role,address=add,mobile=mn)
		return redirect('/usermanage/')
	return render(request,'userupdate.html',{'userd':user,'user':us})

#=======================================================================================================================================================

def managerest(request):
	try:
		user=UserDetails.objects.get(user=request.user)
		if user.role=='admin':
			rest=Restaurants.objects.all()
			return render(request,'managerest.html',{'rest':rest})
		else:
			return redirect('/')
	except:
		return redirect('/')

#==============================================================================================================================================================

def restremove(request,id):
	rest=Restaurants.objects.get(id=id)
	userd=rest.user.id
	user=rest.user.user.id
	re=Restaurants.objects.filter(id=rest.id)
	re.delete()
	userd1=UserDetails.objects.filter(id=userd)
	userd1.delete()
	user1=User.objects.filter(id=user)
	user1.delete()
	return redirect('/managerestursnt/')

#=========================================================================================================================================================

def restupdate(request,id):
	rest=Restaurants.objects.get(id=id)
	if request.method=='POST':
		hn=request.POST['hn']
		de=request.POST['de']
		lo=request.POST['lo']
		rest1=Restaurants.objects.filter(id=id)
		rest1.update(name=hn,details=de,location=lo)
		return redirect('/managerestursnt/')
	return render(request,'updaterest.html',{'rest':rest})

#=============================================== forget password ===========================================================================================================

def forget(request,id):
	a=1
	if str(request.user) == "AnonymousUser":
		a = 0
	msg=''
	data = 1
	if request.method == 'POST':
		otp=random.randint(1000,9999)
		data = 2
		otp=str(otp)
		email =request.POST['email']
		uname=request.POST['uname']
		msg='hello'
		subject = 'Thank you for choosing Yami Food Delivery'
		message = 'Your OTP is :- '+str(otp)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]
		send_mail( subject, message, email_from, recipient_list )
		




		return render(request, 'forget.html',{'msg':msg,'data':data,'otp':otp,'email':email,'uname':uname,'not':a})
	return render(request, 'forget.html',{'msg':msg,'data':data,'non':id,'not':a})

#=============================================== Email otp ==================================================================================================

def otp(request):
	otp1=request.POST['otp1']
	otpreal=request.POST['otpreal']
	pas=request.POST['pas']
	email=request.POST['email']
	uname=request.POST['usname']
	if int(otp1)==int(otpreal):
		user=User.objects.filter(username=uname)
		user.update(password=make_password(pas))
		return redirect('/login/')
	else:
		return HttpResponse('<a href="/forget/1" style="color:red"> invalid OTP </a>')

#=========================================== Social Login =========================================================================================

def social(request):
	try:
		user=UserDetails.objects.get(user__username=request.user)
		return redirect('/')
	except:
		user=User.objects.get(username=request.user)
		add="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14661.573440403501!2d77.4040640197754!3d23.26515250000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x397c683060e9aceb%3A0xefd1f36eaca53265!2sBhopal%20Jn.!5e0!3m2!1sen!2sin!4v1624970684755!5m2!1sen!2sin"
		city=City.objects.get(id=1)
		userd=UserDetails(role='user',user=user,city=city,address=add)
		userd.save()
		return redirect('/')

#========================================== Total collection ========================================================================================================

def totalcollection(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'admin':
			book=Booking.objects.all()
			a=0
			data={}
			for i in book:
				x=int(i.food.price) * int(i.qty)
				a+=x
				data[i.bookingid[:8]] = data.get(i.bookingid[:8],0)+x
			return render(request,'ordercounter.html',{'data':data,'a':a})
		else:
			return redirect('/')
	except:
		return redirect('/')

#===================================================================================================================================================

def usersearch(request):
	userdata=[]
	if request.method =='POST':
		search=request.POST['search']
		user1=UserDetails.objects.all()
		userdata=[]
		for i in user1:
			if search in i.user.username:
				userdata.append(i)
		return render(request,'usersearch.html',{'user1':userdata})
	return render(request,'usersearch.html')