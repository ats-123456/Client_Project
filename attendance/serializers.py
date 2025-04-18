from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import UserProfile


from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



from rest_framework import serializers
# from .models import StaffAssignment

# class StaffAssignmentSerializer(serializers.ModelSerializer):
#     staff_username = serializers.CharField(source='staff.username', read_only=True)
#     class_name = serializers.CharField(source='assigned_class.cname.name', read_only=True)
#     year = serializers.CharField(source='assigned_class.year', read_only=True)
#     section = serializers.CharField(source='assigned_class.section', read_only=True)

#     class Meta:
#         model = StaffAssignment
#         fields = ['s_id', 'staff', 'staff_username', 'assigned_class', 'class_name', 'year', 'section']
#         extra_kwargs = {
#             'assigned_class': {'write_only': True}
#         }

from rest_framework import serializers
from .models import StaffAssignment,Student


class StaffAssignmentSerializer(serializers.ModelSerializer):
    staff_username = serializers.CharField(source='staff.username', read_only=True)
    class_name = serializers.CharField(source='assigned_class.cname.name', read_only=True)
    year = serializers.CharField(source='assigned_class.year', read_only=True)
    section = serializers.CharField(source='assigned_class.section', read_only=True)
    s_id = serializers.CharField(source='staff.s_id', read_only=True)  # Add s_id field to be serialized

    class Meta:
        model = StaffAssignment
        fields = ['s_id', 'staff', 'staff_username', 'assigned_class', 'class_name', 'year', 'section']
        extra_kwargs = {
            'assigned_class': {'write_only': True}
        }



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id','name','roll_number','email','class_info']











# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['phone_number', 'address']


# from django.contrib.auth.models import User
# from rest_framework import serializers

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password']
#         )
#         return user