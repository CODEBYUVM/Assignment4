from django.urls import path
from . import views

urlpatterns =[
    path('', views.say_hello),
    path('add', views.add, name='add')
]