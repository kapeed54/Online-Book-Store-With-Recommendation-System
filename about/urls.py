from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_detail, name='about_detail'),
    ]
   