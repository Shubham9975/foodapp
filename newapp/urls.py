from django.urls import path, include
from . import views

urlpatterns = [
    path('addition', views.home, name='home'),
    path('add', views.add, name='add'),
]