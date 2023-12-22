from django.db import models
from django.contrib import admin
# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    received_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} -{self.received_on}"

    class Meta:
        db_table = 'Contactus'


@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',
                    'subject', 'message', 'received_on')
    search_fields = ['received_on', 'email']
    list_filter = ['received_on']


class BookAppontment(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        db_table = 'BookAppontment'


@admin.register(BookAppontment)
class BookAppontmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'time', 'date',
                    'age', 'gender', 'address', 'message')
    search_fields = ['date', 'name', 'email', 'phone']
    list_filter = ['date']

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()
    received_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} -{self.received_on}"

    class Meta:
        db_table = 'Enquiry'


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',
                    'message', 'received_on')
    search_fields = ['received_on', 'email']
    list_filter = ['received_on']

class Packages(models.Model):
    package_name=models.CharField(max_length=150)
    image=models.ImageField( upload_to='packages')
    price=models.BigIntegerField()
    includeds=models.TextField()
    class Meta:
        db_table='Packages'
@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display=('package_name','image','price','includeds')
    search_fields=['package_name','price']
    list_filter=['package_name']