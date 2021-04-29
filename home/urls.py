from django.urls import path
from .import views

from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('user-register/', views.userregisted, name="userregisted"),  
    path('Hotel/', views.hotel,name='hotel'), 
    path('Travel/', views.travel,name='travel'),        
    path('Currency/', views.currency,name='currency'),      
    path('Mokoro/', views.mokoro,name='mokoro'),
     path('Boat/', views.boat,name='boat'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
 


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)