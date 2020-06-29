from django.urls import path
from . import views


urlpatterns=[

path('customer/', views.customer_payment_history, name="customer_payment_history"),
path('list/', views.payment_history_list, name="payment_history_list"),

	


]