from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('json/<int:size>/', views.getData, name='getdata'),
    path('add/', views.addData),
    path('json/all/', views.getAllData),
]