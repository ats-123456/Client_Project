from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username




CATEGORY_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]

class classroom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Year(models.Model):
    cname = models.ForeignKey(classroom,on_delete=models.CASCADE)
    year = models.CharField(max_length=30)
    section = models.CharField(max_length=30,choices=CATEGORY_CHOICES,default='a')


    def __str__(self):
        return self.cname.name

