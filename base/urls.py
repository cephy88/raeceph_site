from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('resume/', views.resume, name='resume'),
]