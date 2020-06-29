from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.update_customer_profile, name="update_customer_profile"),
path('manager/', views.update_manager_profile, name="update_manager_profile"),

	


]