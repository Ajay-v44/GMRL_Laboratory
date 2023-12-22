from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
   try:
      status=False
      if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            if name or email or phone or message != "":
                Enquiry.objects.create(
                    name=name, email=email, phone=phone,  message=message)
                status = True
                messages.info(
                    request, 'Sent Succesfully.We Will Get Back To You Soon')
            else:
                status = False
                messages.info(request, 'Sorry Error Occured ! Please Try Again')
                return redirect(index)


      return render(request, 'index.html',{'status':status})
   except Exception as e:
       return render(request,'404.html')



def aboutus(request):
    return render(request, 'aboutus.html')


def testpage(request):
    return render(request, 'tests.html')


def packages(request):
    try:
        query=Packages.objects.all()
        return render(request, 'packages.html',{"query":query})
    except Exception as e:
       return render(request,'404.html')


def blogs(request):
    try:
     query=Blogs.objects.all()
     return render(request, 'blogs.html',{"query":query})
    except Exception as e:
       
       return render(request,'404.html')



def gallery(request):

    return render(request, 'gallery.html')


def branches(request):
    return render(request, 'branches.html')


def contact_us(request):
    try:
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
    except:
       return render(request,'404.html')


def book_appontment(request):
    try:
        status=False
        if request.method=="POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            time=request.POST['time']
            date=request.POST['date']
            age=request.POST['age']
            gender=request.POST['gender']
            address = request.POST['address']
            message = request.POST['message']
            if name or email or phone or time or date or age or gender or address or message !="":
                query=BookAppontment.objects.create(name=name,email=email,phone=phone,time=time,date=date,age=age,gender=gender,address=address,message=message)
                if query:
                    status=True
                    messages.success(request,"SUccessfull Booked.")
                else:
                    messages.error(request,'Sorry Error Occured Please Try Again')
            else:
                messages.error(request,"Sorry Null Values Are Not Allowed")
                return redirect(book_appontment)

        return render(request, 'bookappointment.html',{"status":status})
    except Exception as e:
       return render(request,'404.html')


def detail_packages(request,id):
    try:
        query=Packages.objects.filter(id=id)
        return render(request, 'detailedpackage.html',{"query":query})
    except Exception as e:
       print(e)
       return render(request,'404.html')


def detail_blogepage(request,id):
    try:
        recent=Blogs.objects.all().order_by('-date')[:5]
        query=Blogs.objects.filter(id=id)
        return render(request, 'detailblogpage.html',{"query":query,"recent":recent})
    except Exception as e:
       return render(request,'404.html')

