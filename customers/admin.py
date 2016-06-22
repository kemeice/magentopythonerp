from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email',  'name', 'address', 'phone_number')
admin.site.register(Customer, CustomerAdmin)