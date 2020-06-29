from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.update_customer_password, name="update_customer_password"),
path('manager/', views.update_manager_password, name="update_manager_password"),

	


]