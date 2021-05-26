from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('books',views.second),
    path('books/<num>' , views.view)
]