from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.check_customer_password, name="check_customer_password"),
path('manager/', views.check_manager_password, name="check_manager_password"),

	


]