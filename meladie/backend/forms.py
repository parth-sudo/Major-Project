from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HeartPatient, DiabetesPatient

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class HeartPatientForm(forms.ModelForm):
    class Meta:
        #todo.
        model = HeartPatient
        fields = '__all__'
        # fields = ['age', 'sex', 'chest_pain_type', 
        #         'resting_blood_pressure', 'cholesterol', 
        #         'fasting_blood_sugar', 'maximum_heart_rate_achieved', 'exercise_induced_angina']


class DiabetesPatientForm(forms.ModelForm):
    class Meta:
        model = DiabetesPatient
        fields = '__all__'