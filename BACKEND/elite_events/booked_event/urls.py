from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.customer_booked_event, name="customer_booked_event"),
path('list/', views.booked_event_list, name="booked_event_list"),

	


]