from django.db import models
from django.contrib.auth.models import User

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





