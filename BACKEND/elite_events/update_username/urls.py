from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.update_customer_username, name="update_customer_username"),
path('manager/', views.update_manager_username, name="update_manager_username"),

	


]