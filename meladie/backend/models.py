from django.db import models
from django.contrib.auth.models import User
import datetime, pytz
from django.utils import timezone
from .extras import GENDER_CHOICE, CHEST_PAIN_CHOICE, TEST_CHOICES, TIME_SLOTS

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)
    information = models.TextField()
    symptoms = models.TextField(default="abc")
    causes = models.TextField(default="abc")
    vulnerable = models.TextField(default="abc")
    food_to_eat = models.TextField() 

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    full_name = models.CharField(max_length=30, blank = False)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=14)
    yoe = models.IntegerField()
    gender = models.CharField(max_length=6)
    rating = models.CharField(max_length=5)
    specialization = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class HeartPatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, blank = False)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male')  
    chest_pain_type = models.CharField(max_length=20, choices = CHEST_PAIN_CHOICE, default='Typical Angina')
    resting_blood_pressure = models.CharField(max_length=3, blank = False)
    cholesterol = models.CharField(max_length=4, blank = False)
    fasting_blood_sugar_greater_than_120 = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')])
    maximum_heart_rate_achieved = models.CharField(max_length=4)
    exercise_induced_angina = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')])
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








