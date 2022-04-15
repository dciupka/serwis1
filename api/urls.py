from django.urls import path
from . import views

urlpatterns = [
    path('json/<int:size>/', views.getData),
    path('add/', views.addData),
    path('json/all/', views.getAllData),
]