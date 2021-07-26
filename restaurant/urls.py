from django.urls import path, include
from . import views
app_name='restaurant'
urlpatterns = [
    path('',views.home, name='home'),
    path('addfood/',views.addfood),
   	path('foodlist/',views.foodlist),
   	path('fooddelete/<int:id>/',views.fooddelete,name='fooddelete'),
   	path('foodupdate/<int:id>/',views.foodupdate,name='foodupdate'),
   	path('tablebook/',views.tablebooks),
   	path('addchef/',views.addchef),
   	path('addimage/',views.addimage),
   	path('removeimage/<int:id>',views.removeimage,name='reimg'),
    path('foodimg/',views.foodimg),
    path('orders/',views.orders),
    path('cancel/<int:id>',views.rescancel,name='cancel'),
    path('chef/',views.chef),
    path('chefdel/<int:id>/',views.chefdel,name='del'),
    path('collection/',views.collection),
    path('currentorder/',views.currentorder),
    path('processed/<int:id>/',views.processed,name='processed'),
    path('ordernow/',views.ordernow),
    path('booking/',views.booking),
    path('staff/',views.staff),
]