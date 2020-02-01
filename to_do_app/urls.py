from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name= 'index'),
    path('index/<list_id>', views.delete, name = 'delete'),
    path('coss_off/<list_id>', views.cross_off, name = 'cross_off'),
    path('uncross_off/<list_id>', views.uncross_off, name = 'uncross_off'),
   
   
]