from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home_view, name='home')
]
