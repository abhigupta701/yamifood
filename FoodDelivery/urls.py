from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

app_path='FoodDelivery'

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('',include('customer.urls')),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin),
    path('adduser/',views.useradd),
    path('add_deli/',views.add_deli),
    path('addrest/',views.addrest),
    path('logout/',views.logout_call),
    path('adminstuff/',views.admins),
    path('addcity/',views.city),
    path('addstate/',views.state),
    path('addaddr/',views.addadder),
    path('restaurant/',include('restaurant.urls')),
    path('customer/',include('customer.urls')),
    path('delivery/',include('delivery.urls')),
    path('verifydelivery/',views.verifyd),
    path('verifyr/',views.verifyr),
    path('verifys/<int:id>/',views.verifys,name='verify'),
    path('usermanage/',views.usermanage),
    path('userremove/<int:id>/',views.userremove,name='userremove'),
    path('userupdate/<int:id>/',views.userupdate,name='userupdate'),
    path('managerestursnt/',views.managerest),
    path('restremove/<int:id>/',views.restremove,name='restremove'),
    path('restupdate/<int:id>/',views.restupdate,name='restupdate'),
    path('counter/',views.totalcollection),
    path('forget/<int:id>',views.forget,name='forget'),
    path('otp/',views.otp),
    path('googlee/',views.social),
    path('usersearch/',views.usersearch),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
