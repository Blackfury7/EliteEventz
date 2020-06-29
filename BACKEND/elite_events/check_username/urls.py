from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.check_customer_username, name="check_customer_username"),
path('manager/', views.check_manager_username, name="check_manager_username"),

	


]