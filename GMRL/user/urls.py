from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('/aboutus',aboutus,name='aboutus')
]
