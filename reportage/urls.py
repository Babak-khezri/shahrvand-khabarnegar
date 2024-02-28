from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'reportage'
urlpatterns = [
    path("reportage/<int:pk>", reportage_detail, name="reportage_detail")

]
