from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('/aboutus',aboutus,name='aboutus'),
    path('/tests',testpage,name='tests'),
    path('/packages',packages,name='packages'),
    path('/blogs',blogs,name='blogs'),
    path('/gallery',gallery,name='gallery'),
    path('/branches',branches,name='branches'),
    path('/contactus',contact_us,name='contactus')
]
