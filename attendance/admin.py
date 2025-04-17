from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Year)
admin.site.register(classroom)
admin.site.register(Staff)