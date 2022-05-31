from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HeartPatient, DiabetesPatient, LiverPatient, Profile
from django.forms import TextInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class HeartPatientForm(forms.ModelForm):
    class Meta:
        #todo.
        model = HeartPatient
        # fields = '__all__'
        fields = ['age', 'sex', 'chest_pain_type', 
                'resting_blood_pressure', 'serum_cholesterol', 
                'fasting_blood_sugar_greater_than_120', 'resting_electrocardiographic_results', 
                'exercise_induced_angina', 'old_peak', 'slope', 'number_of_major_vessels_coloured_by_flouroscopy']

        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }

class DiabetesPatientForm(forms.ModelForm):
    class Meta:
        model = DiabetesPatient
        # fields = '__all__'
        fields = ['glucose', 'blood_pressure', 'insulin', 'body_mass_index', 'age']
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }

class LiverPatientForm(forms.ModelForm):
    class Meta:
        model = LiverPatient
        fields = ['age', 'gender', 'total_bilirubin', 'alkaline_phosphotase', 'alamine_aminotransferase', 'total_protiens', 'albumin']
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }



    