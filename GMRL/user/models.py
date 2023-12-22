from django.db import models
from django.contrib import admin
# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
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
