from django.db import models
from django.contrib.auth.models import User
import datetime, pytz
from django.utils import timezone

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)
    information = models.TextField()
    food_to_eat = models.TextField() 

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    tests_taken = models.IntegerField(default=0)

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

GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

CHEST_PAIN_CHOICE = (
      ('Typical Angina', 'Typical Angina'),
      ('Atypical Angina', 'Atypical Angina'),
      ('Non-Anginal Pain', 'Non-Anginal Pain'),
      ('Asymptomatic', 'Asymptomatic'),
)

class HeartPatient(models.Model):
    #default.
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, blank = False)
    sex = models.CharField(max_length=6, choices=GENDER_CHOICE, default='Male')  
    chest_pain_type = models.CharField(max_length=20, choices = CHEST_PAIN_CHOICE, default='Typical Angina')
    resting_blood_pressure = models.CharField(max_length=3, blank = False)
    cholesterol = models.CharField(max_length=4, blank = False)
    fasting_blood_sugar = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')])
    maximum_heart_rate_achieved = models.CharField(max_length=4)
    exercise_induced_angina = models.CharField(max_length=10, choices=[('True', 'True'), ('False', 'False')])
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_profile.user.username


class DiabetesPatient(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    glucose = models.CharField(max_length = 3, blank=False)
    blood_pressuse = models.CharField(max_length = 3, blank=False)
    insulin = models.CharField(max_length = 3, blank=False)
    body_mass_index = models.CharField(max_length=4, blank=False)
    age = models.CharField(max_length=3, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_profile.user.username









