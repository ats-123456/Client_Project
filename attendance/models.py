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

years = [
    ('1st Year','1st Year'),
    ('2nd Year','2nd Year'),
    ('3rd Year','3rd Year'),
    ('4th Year','4th Year')
] 

class classroom(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    cname = models.ForeignKey(classroom, on_delete=models.CASCADE)
    year = models.CharField(max_length=30, choices=years)
    section = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='a')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cname', 'year', 'section'], name='unique_class_year_section')
        ]

    def clean(self):
        if Year.objects.filter(
            cname=self.cname,
            section=self.section,
            year__iexact=self.year  # case-insensitive check
        ).exclude(pk=self.pk).exists():
            raise ValidationError("This combination of class, year, and section already exists (case-insensitive).")

    def save(self, *args, **kwargs):
        self.full_clean()  # just this, don't lower the year
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cname.name} - {self.year} - {self.section}"
