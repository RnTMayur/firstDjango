from django.contrib import admin
from .models import comapny
# Register your models here.

class comapnyItem(admin.ModelAdmin):
    list_display=('name','contact','country')

admin.site.register(comapny,comapnyItem)