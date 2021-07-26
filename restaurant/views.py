from django.shortcuts import render, redirect
from restaurant.models import *
from customer.models import *
import datetime
# Create your views here.

#==================================== Restaurant Home =========================================================================
def home(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			book=Booking.objects.filter(rest__user__user__username=request.user)
			a=0
			data={}
			for i in book:
				x=int(i.food.price) * int(i.qty)
				a+=x
				data[i.bookingid[:8]] = data.get(i.bookingid[:8],0)+x/10
			
			user=UserDetails.objects.get(user=request.user)
			rest=Restaurants.objects.get(user=user)
			return render(request,'restaurant/restaurant.html',{'rest':rest,'data':data,'total':a})
		else:
			return redirect('/')
	except Exception as e:
		print(e)
		return redirect('/')

#========================================== Add Food ==========================================================================

def addfood(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			user=UserDetails.objects.get(user__username=request.user)
			fc = FoodCategory.objects.all()
			ft = FoodType.objects.all()
			food=Food.objects.all()
			if request.method=='POST':
				name=request.POST['nm']
				details=request.POST['details']
				fcategory=request.POST['fcat']
				ftype=request.POST['ftype']
				img=request.FILES['img']
				price=request.POST['price']
				rest=Restaurants.objects.get(user=user)
				fc1 = FoodCategory.objects.get(id=fcategory)
				ft1 = FoodType.objects.get(id=ftype)
				f=Food(name=name, details=details, fcategory=fc1, ftype=ft1, restaurant=rest, image=img, price=price)
				f.save()
			return render(request,'restaurant/addfood.html',{'data':ft,'data1':fc,'food':food})
		else:
			return redirect('/')
	except:
		return redirect('/')

#========================================= FoodImage ===============================================================================

def foodimg(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			img1=request.FILES['img1']
			img2=request.FILES['img2']
			img3=request.FILES['img3']
			fd=request.POST['fname']
			food=Food.objects.get(id=fd)
			print(food)
			rest=Restaurants.objects.get(user__user__username=request.user)
			for i in [img1,img2,img3]:
				fimg=FoodImage(restaurant=rest,image=i,food=food)
				fimg.save()
			return redirect('/restaurant/addfood/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#===================================================== Foodlist =============================================================================

def foodlist(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			user = UserDetails.objects.get(user__username=request.user)
			rest = Restaurants.objects.get(user=user)
			food = Food.objects.filter(restaurant=rest)
			return render(request,'restaurant/foodlist.html',{'food':food})
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================== Food Delete ===========================================================================

def fooddelete(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			f = Food.objects.filter(id=id)
			f.delete()
			return redirect('/restaurant/foodlist/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#===================================================== Food Update =================================================================

def foodupdate(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			f=Food.objects.update(id=id)
			if request.method == 'POST':
				name=request.POST['nm']
				details=request.POST['details']
				price=request.POST['price']
				f.update(name=name,details=details,price=price)
				return redirect('/addlist/')
			return render(request,'restaurant/foodupdate.html',{'food':f})
	except:
		return redirect('/')

#=============================================== Table Book ===================================================================

def tablebooks(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			user = UserDetails.objects.get(user__username=request.user)
			rest = Restaurants.objects.get(user=user)
			book = Reservation.objects.filter(rest=rest)
			return render(request,'restaurant/tablebook.html',{'data':book})
		else:
			return redirect('/')
	except:
		return redirect('/')

#==================================================== Booking Cancel ==========================================================================

def bookingcancel(request,id):
	t=tablebook.objects.filter(id=id)	
	t.delete()
	return redirect('/restaurant/tablebook/')

#===================================================== Add Chef ==================================================================================

def addchef(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			user = UserDetails.objects.get(user__username=request.user)
			rest = Restaurants.objects.get(user=user)
			if request.method=='POST':
				name=request.POST['name']
				posts=request.POST['post']
				img=request.FILES['img']
				c=RestChefs(name=name,post=posts,resto=rest,img=img)
				c.save()
			return render(request,'restaurant/addchef.html')
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================ Add Image ============================================================================

def addimage(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role) == 'restaurant':
			user=UserDetails.objects.get(user__username=request.user)
			rest=Restaurants.objects.get(user=user)
			ri=RestImg.objects.filter(resto=rest)
			if request.method == 'POST':
				img=request.FILES['img']
				r=RestImg(img=img,resto=rest)
				r.save()
			return render(request,'restaurant/addimage.html',{'image':ri})
		else:
			return redirect('/')
	except:
		return redirect('/')

#========================================================= Delete Image ===========================================================

def removeimage(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			img=RestImg.objects.get(id=id)
			img.delete()
			return redirect('/restaurant/addimage/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#=============================================================== Order ===================================================================

def orders(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			book = Booking.objects.filter(rest__user__user__username=request.user)
			return render(request,'restaurant/order.html',{'book':book})
		else:
			return redirect('/')
	except:
		return redirect('/')

#======================================================== Restaurant Delete ===================================================

def rescancel(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			res=Reservation.objects.get(id=id)
			res.delete()
			return redirect('/restaurant/tablebook/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================= Chef ==============================================================================

def chef(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			chef=RestChefs.objects.filter(resto__user__user__username=request.user)
			return render(request,'restaurant/chef.html',{'chef':chef})
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================== Chef Delete ======================================================================

def chefdel(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			chef=RestChefs.objects.get(id=id)
			chef.delete()
			return redirect('/restaurant/chef/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================== Total Collection ==========================================================================

def collection(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			book=Booking.objects.filter(rest__user__user__username=request.user)
			a=0
			data={}
			for i in book:
				x=int(i.food.price) * int(i.qty)
				a+=x
				data[i.bookingid[:8]] = data.get(i.bookingid[:8],0)+x
			return render(request,'restaurant/collection.html',{'data':data,'a':a})
		else:
			return redirect('/')
	except:
		return redirect('/')

#============================================== Current Order ==========================================================================

def currentorder(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			book1 = Booking.objects.filter(rest__user__user__username=request.user)
			book=[]
			for i in book1:
				if i.status==0:
					book.append(i)
			return render(request,'restaurant/currentorder.html',{'book':book})
		else:
			return redirect('/')
	except:
		return redirect('/')

#=================================================== Processed ====================================================================================

def processed(request,id):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			booking=Booking.objects.filter(id=id)
			booking.update(status=1)
			return redirect('/restaurant/currentorder/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================= Order Now =========================================================================================

def ordernow(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			food=Food.objects.filter(restaurant__user__user__username=request.user)
			return render(request,'restaurant/ordernow.html',{'food':food})
		else:
			return redirect('/')
	except:
		return redirect('/')

#================================================ Booking =============================================================================================

def booking(request):
	try:
		user=UserDetails.objects.get(user = request.user)
		if str(user.role)== 'restaurant':
			fid=request.POST['fid']
			qty=request.POST['qty']
			oid=datetime.datetime.today()#date object
			x = str(oid).replace("-","").replace(' ','').replace(':','').replace('.','')#Creating Order ID
			food=Food.objects.get(id=fid)
			rest=Restaurants.objects.get(user__user__username=request.user)
			user=UserDetails.objects.get(user__username=request.user)
			deliv=Deliveryboy.objects.get(id=4)
			book=Booking(bookingid=x,food=food,rest=rest,qty=qty,status=0,user=user,delivboy=deliv,delevirytime='OurOrder')
			book.save()
			return redirect('/restaurant/ordernow/')
		else:
			return redirect('/')
	except:
		return redirect('/')

#===================================================== Restaurant Staff ==============================================================================================================

def staff(request):
	staff=Staff.objects.filter(rest__user__user__username=request.user)
	if request.method=='POST':
		name=request.POST['name']
		salary=request.POST['salary']
		post=request.POST['post']
		rest=Restaurants.objects.get(user__user__username=request.user)
		s=Staff(salary=salary,post=post,name=name,rest=rest)
		s.save()
	return render(request,'restaurant/staff.html',{'staff':staff})
