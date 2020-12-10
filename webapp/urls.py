"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('login/', views.userlogindef, name="userlogindef"),
    path('signup/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhomedef"),
    path('userlogout/', views.userlogoutdef, name="userlogoutdef"),
    path('viewrooms/', views.viewrooms, name="viewrooms"),
    path('check/', views.check, name="check"),
    path('booking/', views.bookingdef, name="bookingdef"),
    path('userhome2/', views.userhomedef2, name="userhomedef2"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
	path('alogin/', views.alogin, name="alogin"),
    path('adminlogindef/', views.adminlogindef, name="adminloginactiondef"),
    path('adminhome/', views.adminhome, name="adminhome"),	
	path('alogout/', views.alogout, name="alogout"),	
    path('aviewrooms/', views.aviewrooms, name="aviewrooms"),    
    
       

    
    
]
