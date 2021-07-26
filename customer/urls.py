from django.urls import path, include
from . import views

app_name='customer'
	
urlpatterns = [
    path('',views.home, name='home'),
    path('rest/<int:id>/',views.rest,name='rest'),
    path('menu/',views.menu),
    path('restaurants/',views.restro),
    path('cart/',views.contact), 
    path('food/<int:id>/',views.item,name='item'),
    path('booking/<int:id>/',views.booking,name='booking'),
    path('cart/<int:id>/',views.cart,name='cart'),
    path('cartr/<int:id>/',views.cartr,name='cartr'),
    path('reserv/<int:id>/',views.reserv,name='reserv'),
    path('profile/',views.profile),
    path('delitem/<int:id>/',views.delitem,name='del'),
    path('rating/',views.urating),
    path('search/',views.search),
    path('cancel/<int:id>',views.ocancel,name='cancel'),
]