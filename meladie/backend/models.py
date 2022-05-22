from django.db import models
from django.contrib.auth.models import User
import datetime, pytz
from django.utils import timezone
from .extras import GENDER_CHOICE, CHEST_PAIN_CHOICE, TEST_CHOICES, TIME_SLOTS

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)
    information = models.TextField(default="information.")
    symptoms = models.TextField(default="symptoms.")
    causes = models.TextField(default="causes.")
    vulnerable = models.TextField(default="vulnerable.")
    food_to_eat = models.TextField(default="green vegetables.") 
    lifestyle_changes = models.TextField(default="Exercise and Meditate.")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    full_name = models.CharField(max_length=30, blank = False, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, default="Delhi")
    contact = models.CharField(max_length=14)
    yoe = models.IntegerField()
    gender = models.CharField(max_length=6)
    rating = models.CharField(max_length=5)
    specialization = models.ForeignKey(Disease, on_delete=models.CASCADE)
    availability = models.CharField(max_length=20, default="10 A.M-11 A.M")

    def __str__(self):
        return self.full_name


class HeartPatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, blank = False)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male')  
    chest_pain_type = models.CharField(max_length=20, choices = CHEST_PAIN_CHOICE, default='Typical Angina')
    resting_blood_pressure = models.CharField(max_length=3, blank = False)
    serum_cholesterol = models.CharField(max_length=4, blank = False)
    fasting_blood_sugar_greater_than_120 = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')], default='False')
    resting_electrocardiographic_results = models.CharField(max_length=20, choices = [('Normal', 'Normal'), ('Having ST-T','Having ST-T'), ('Hypertrophy','Hypertrophy')], default="Normal")
    exercise_induced_angina = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')], default='False')
    old_peak = models.CharField(max_length=5, default="1.1")
    slope = models.CharField(max_length=5, default="2")
    number_of_major_vessels_coloured_by_flouroscopy = models.CharField(max_length=1, default="2")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


class DiabetesPatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose = models.CharField(max_length = 3, blank=False)
    blood_pressure = models.CharField(max_length = 3, blank=False)
    insulin = models.CharField(max_length = 3, blank=False)
    body_mass_index = models.CharField(max_length=4, blank=False)
    age = models.CharField(max_length=3, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class LiverPatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male') 
    total_bilirubin = models.CharField(max_length=5)
    alkaline_phosphotase = models.CharField(max_length=5)
    alamine_aminotransferase = models.CharField(max_length=5)
    total_protiens = models.CharField(max_length=4)
    albumin = models.CharField(max_length=4)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class BookLabTest(models.Model):
    full_name = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=14, blank=False)
    test_name = models.CharField(max_length=60, default='Basic Metabolic Panel')
    time_slot = models.CharField(max_length=20, default='11AM - 12PM')
    date = models.DateField()

    def __str__(self):
        return self.full_name

class BookDoctorAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=20, default='10.AM')
    date = models.DateField()
    time_of_creation = models.DateTimeField(null = False, blank = False, auto_now_add=True)

    def __str__(self):
        return self.user.username










