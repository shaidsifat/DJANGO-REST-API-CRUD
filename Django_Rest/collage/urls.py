




    
    

from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home1 , name='home'),
    path('product/', views.product , name='product'),
    path('product/<int:pk>/',views.product_detail,name='product_detail'), 

]