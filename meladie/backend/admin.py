from django.contrib import admin
from .models import BookDoctorAppointment, Disease, Profile, Doctor, HeartPatient, DiabetesPatient, LiverPatient, BookLabTest
# Register your models here.
admin.site.register(Disease)
admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(HeartPatient)
admin.site.register(DiabetesPatient)
admin.site.register(LiverPatient)
admin.site.register(BookLabTest)
admin.site.register(BookDoctorAppointment)