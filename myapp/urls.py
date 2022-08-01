from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views 


urlpatterns = [ 
    path('', views.index),
    path('contact/', views.contact,name='contact'),
    path('userlogout/',views.userlogout),
    path('updateprofile/',views.updateprofile),
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
]   
   