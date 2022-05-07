from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, HeartPatientForm, DiabetesPatientForm
from django.contrib.auth.models import User
from .models import Profile
from .predictions import heart_disease, diabetes

def home(request):
    return render(request, 'backend/home.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'The account for {username} has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'backend/register.html', {'form':form})

def analyze(request):
    #todo
    return render(request,'backend/analyze.html', {})

@login_required
def heart_disease_prediction(request):
    context = {}
    if request.method == 'POST':
        form = HeartPatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = form
            age=form.cleaned_data.get('age')
            sex=form.cleaned_data.get('sex')
            chest_pain_type=form.cleaned_data.get('chest_pain_type')
            resting_blood_pressure=form.cleaned_data.get('resting_blood_pressure')
            cholesterol=form.cleaned_data.get('cholesterol')
            fasting_blood_sugar = form.cleaned_data.get('fasting_blood_sugar')
            maximum_heart_rate_achieved = form.cleaned_data.get('maximum_heart_rate_achieved')
            exercise_induced_angina = form.cleaned_data.get('exercise_induced_angina')

            result = heart_disease(age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, maximum_heart_rate_achieved, exercise_induced_angina)
            # result = 1
            print("printing result")
            print(result)
            answer = "Yes, you have a heart disease sadly." if result == 1 else "No, you don't have heart disease."
            context['answer'] = answer
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = HeartPatientForm()
    return render(request,'backend/disease_prediction.html', {'form' : form, 'answer' : ""})

def diabetes_prediction(request):
    context = {}
    if request.method == 'POST':
        form = DiabetesPatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = form
            glucose=form.cleaned_data.get('glucose')
            blood_pressuse=form.cleaned_data.get('blood_pressuse')
            insulin=form.cleaned_data.get('insulin')
            body_mass_index=form.cleaned_data.get('body_mass_index')
            age=form.cleaned_data.get('age')

            result = diabetes(glucose, blood_pressuse, insulin, body_mass_index, age)
            # result = 1
            print("printing result")
            print(result)
            answer = "Yes, you have a diabetes sadly." if result == 1 else "No, you don't have diabetes."
            context['answer'] = answer
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = DiabetesPatientForm()
    return render(request,'backend/disease_prediction.html', {'form' : form, 'answer' : ""})

def disease_information(request):
    #todo
    return render(request,'backend/disease_information.html', {})

def profile(request):
    context = {}
    current_user = request.user
    print(current_user)
    # user = get_object_or_404(User, pk=pk)
    # print(user)
    print(current_user.id)
    profile = Profile.objects.filter(user = current_user)
 
    print(profile)
    # print(user_profile.tests_taken)
    if not profile.exists():
        user_profile = Profile.objects.create(user=current_user, tests_taken=0)
        context['user_profile'] = user_profile 
        return render(request, 'backend/profile.html', {})

    user_profile = Profile.objects.filter(user = current_user)[0]
    context['user_profile'] = user_profile    
    return render(request, 'backend/profile.html', context)

def about(request):
    return render(request,'backend/about.html',{'title':'About'})