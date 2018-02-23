from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'', views.home, name='home'),
    url(r'play', views.play, name='play'),
]
