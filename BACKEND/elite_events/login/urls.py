from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.customer_login, name="customer_login"),
path('manager/', views.manager_login, name="manager_login"),

	


]