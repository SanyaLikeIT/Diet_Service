"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", views.registration, name="registration"),
    path("", views.index_page, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dish/", views.dish, name="dish"),
    path("plan_of_day/", views.plan_of_day, name="plan_of_day"),
    path("plan_of_day/ration/<ration_id>", views.ration, name="ration/<ration_id>"),
    path("dish_list/", views.dish_list, name="dish_list"),
    path("profile/", views.profile, name="profile"),
    path("new_dish/", views.new_dish, name="new_dish"),
    path("current_dish/<dish_id>", views.current_dish, name="current_dish/<id>"),
    path("filtered_dish/<filter_id>", views.filtred_dish, name="filtered_dish/<filter_id>"),
]
