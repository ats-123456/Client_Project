# test_api.py
import requests

BASE_URL = "https://attendance-ghip.onrender.com"

# GET students
def get_students():
    response = requests.get(f"{BASE_URL}/students/")
    if response.status_code == 200:
        print("✅ Students List:")
        for student in response.json():
            print(student)
    else:
        print("❌ Error:", response.status_code, response.text)

# POST student
def create_student():
    data = {
        "name": "Mohan Raj",
        "roll_number": "12345",
        "email": "mohan@example.com"
    }
    response = requests.post(f"{BASE_URL}/students/", json=data)
    if response.status_code == 201:
        print("✅ Student Created:", response.json())
    else:
        print("❌ Error:", response.status_code, response.text)

# GET attendance
def get_attendance():
    response = requests.get(f"{BASE_URL}/attendance/")
    print(response.json())

# POST attendance
def create_attendance():
    data = {
        "student": 1,  # student ID (must already exist)
        "date": "2025-04-15",
        "is_present": True
    }
    response = requests.post(f"{BASE_URL}/attendance/", json=data)
    if response.status_code == 201:
        print("✅ Attendance Marked:", response.json())
    else:
        print("❌ Error:", response.status_code, response.text)


# Call functions
get_students()
create_student()
get_attendance()
create_attendance()
