from django.urls import path, include
from . import views
app_name='delivery'
urlpatterns = [
    
    path('',views.home, name='home'),
    path('order/',views.order),
    path('status/<int:id>',views.status,name='status'),
    path('history/',views.history),

    

]