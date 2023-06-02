from django.urls import path
from app1.views import *

app_name='app1'
urlpatterns=[
    path('kf/',kf,name='kf'),
    path('knock/',knock,name='knock'),
]