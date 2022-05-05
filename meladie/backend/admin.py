from django.contrib import admin
from .models import Disease, Profile, Doctor
# Register your models here.
admin.site.register(Disease)
admin.site.register(Profile)
admin.site.register(Doctor)