"""elite_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    path('add_to_cart/', include('add_to_cart.urls')),
    path('show_cart_element/', include('show_cart_element.urls')),
    path('place_order/', include('place_order.urls')),
    path('booked_event/', include('booked_event.urls')),
    path('check_username/', include('check_username.urls')),
    path('check_password/', include('check_password.urls')),
    path('update_username/', include('update_username.urls')),
    path('update_password/', include('update_password.urls')),
    path('update_profile/', include('update_profile_details.urls')),
    path('payment_history/', include('payment_history.urls')),
]
