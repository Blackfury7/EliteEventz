from django.urls import path
from . import views


urlpatterns=[

path('', views.show_cart_element, name="show_cart_element")

	


]