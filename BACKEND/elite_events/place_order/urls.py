from django.urls import path
from . import views


urlpatterns=[

path('confirm/', views.confirm_order, name="confirm_order"),
path('remove/', views.remove_order, name="remove_order"),

]