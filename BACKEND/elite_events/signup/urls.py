from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.customer_signup, name="customer_signup"),
path('manager/', views.manager_signup, name="manager_signup"),

	


]