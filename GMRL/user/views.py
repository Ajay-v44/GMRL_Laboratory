from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def testpage(request):
    return render(request, 'tests.html')


def packages(request):
    return render(request, 'packages.html')


def blogs(request):
    return render(request, 'blogs.html')


def gallery(request):

    return render(request, 'gallery.html')


def branches(request):
    return render(request, 'branches.html')


def contact_us(request):
    status = True
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        if name or email or phone or subject or message != " ":
            Contactus.objects.create(
                name=name, email=email, phone=phone, subject=subject, message=message)
            status = True
            messages.info(
                request, 'Sent Succesfully.We Will Get Back To You Soon')
            return redirect(contact_us)
        else:
            status = False
            messages.info(request, 'Sorry Error Occured ! Please Try Again')
            return redirect(contact_us)

    return render(request, 'contactus.html', {"status": status})


def book_appontment(request):
    
    return render(request, 'bookappointment.html')


def detail_packages(request):
    return render(request, 'detailedpackage.html')


def detail_blogepage(request):
    return render(request, 'detailblogpage.html')
