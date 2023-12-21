from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def testpage(request):
    return render(request,'tests.html')
def packages(request):
    return render(request,'packages.html')