from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('/aboutus',aboutus,name='aboutus'),
    path('/tests',testpage,name='tests'),
    path('/packages',packages,name='packages')
]
