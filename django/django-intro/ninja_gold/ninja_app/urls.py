from django.urls import path
from . import views

urlpatterns = [
    path('', views.first),
    path('process_money', views.second)

 ]