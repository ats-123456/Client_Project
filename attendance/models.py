from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username



from django.core.exceptions import ValidationError






CATEGORY_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]

class classroom(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    cname = models.ForeignKey(classroom,on_delete=models.CASCADE)
    year = models.CharField(max_length=30)
    section = models.CharField(max_length=30,choices=CATEGORY_CHOICES,default='a')



    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cname', 'year', 'section'], name='unique_class_year_section')
        ]

    def clean(self):
        if Year.objects.filter(cname=self.cname, year=self.year, section=self.section).exclude(pk=self.pk).exists():
            raise ValidationError("This combination of class, year, and section already exists.")

    def save(self, *args, **kwargs):
        self.full_clean()  # This calls clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cname.name} - {self.year} - {self.section}"


