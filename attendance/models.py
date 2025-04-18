from django.db import models
from django.contrib.auth.hashers import make_password, check_password
class Staff(models.Model):

    ROLE_CHOICES = (
        ('staff', 'Staff'),
        ('hod', 'HOD'),
    )
    s_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)  # Will be hashed
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    staff_id = models.CharField(max_length=20, blank=True, null=True,unique=True)
    hod_id = models.CharField(max_length=20, blank=True, null=True)

    @property
    def id(self):  # ✅ Add this property
        return self.s_id


    def save(self, *args, **kwargs):
        # Hash the password only if it's not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def __str__(self):
        return f"{self.username} - {self.role}"






from django.contrib.auth.models import User  # This is important!

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # This is correct
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username









# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username



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
    name = models.CharField(max_length=30)  # Removed unique=True

    def clean(self):
        # Case-insensitive uniqueness check
        if classroom.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'__all__': ["This classroom name already exists (case-insensitive)."]})

    def save(self, *args, **kwargs):
        self.name = self.name.lower()  # normalize input
        self.full_clean()  # runs the clean() method
        super().save(*args, **kwargs)

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


class StaffAssignment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assigned_class = models.ForeignKey(Year, on_delete=models.CASCADE)  # This includes class, year, and section

    class Meta:
        unique_together = ('staff', 'assigned_class')  # Prevents duplicate assignments

    def __str__(self):
        return f"{self.staff.username} -> {self.assigned_class}"





class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    class_info = models.ForeignKey(Year, on_delete=models.CASCADE)  # same as assigned_class

    def __str__(self):
        return f"{self.name} - {self.roll_number}"