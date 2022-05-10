from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, HeartPatientForm, DiabetesPatientForm, LiverPatientForm
from django.contrib.auth.models import User
from .models import Profile, HeartPatient, DiabetesPatient, Disease, LiverPatient
from .predictions import heart_disease, diabetes, liver_disease


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


@login_required
def heart_disease_prediction(request):
    context = {}
    if request.method == 'POST':
        form = HeartPatientForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
   
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
        
            request.session['isHeartPatient'] = True if result == 1 else False

            answer = "Heart Disease detected." if result == 1 else "No, you don't have heart disease."
            context['answer'] = answer
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = HeartPatientForm()
    return render(request,'backend/disease_prediction.html', {'form' : form, 'answer' : ""})

@login_required
def diabetes_prediction(request):
    context = {}
    if request.method == 'POST':
        form = DiabetesPatientForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print(form)

            context['form'] = form
            glucose=form.cleaned_data.get('glucose')
            blood_pressure=form.cleaned_data.get('blood_pressure')
            insulin=form.cleaned_data.get('insulin')
            body_mass_index=form.cleaned_data.get('body_mass_index')
            age=form.cleaned_data.get('age')

            result = diabetes(glucose, blood_pressure, insulin, body_mass_index, age)
       
            request.session['isDiabetesPatient'] = True if result == 1 else False
            answer = "You have diabetes." if result == 1 else "No, you don't have diabetes."
            context['answer'] = answer
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = DiabetesPatientForm()
    return render(request,'backend/disease_prediction.html', {'form' : form, 'answer' : ""})

@login_required
def liver_prediction(request):
    context = {}
    if request.method == 'POST':
        form = LiverPatientForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            context['form'] = form
          
            age=form.cleaned_data.get('age')
            gender=form.cleaned_data.get('gender')
            total_bilirubin = form.cleaned_data.get('total_bilirubin')
            alkaline_phosphotase=form.cleaned_data.get('alkaline_phosphotase')
            alamine_aminotransferase=form.cleaned_data.get('alamine_aminotransferase')
            total_protiens=form.cleaned_data.get('total_protiens')
            albumin=form.cleaned_data.get('albumin')

            result = liver_disease(age, gender, total_bilirubin, alkaline_phosphotase, alamine_aminotransferase, total_protiens, albumin)
            request.session['isLiverPatient'] = True if result == 1 else False

            answer = "Yes, you have a liver disease sadly." if result == 1 else "No, you don't liver disease."
            context['answer'] = answer
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = LiverPatientForm()
    return render(request,'backend/disease_prediction.html', {'form' : form, 'answer' : "",'user_profile' : instance})

def disease_information(request, disease_name):
    context = {}
    if disease_name == "heart_disease":
        heart = Disease.objects.filter(name="Heart Disease")[0]
        context['disease_name'] = 'Heart Disease'
        context['object'] = heart
    elif disease_name == "diabetes":
        diabetes = Disease.objects.get(pk = 2)
        context['disease_name'] = 'Diabetes'
        context['object'] = diabetes
    elif disease_name == "liver_disease":
        liver = Disease.objects.get(pk = 3)
        context['disease_name'] = 'Liver Disease'
        context['object'] = liver

    return render(request, 'backend/disease_information.html', context) 


def profile(request):
    context = {}
    current_user = request.user
    print(current_user.email)
  
    profile = Profile.objects.filter(user = current_user)

    if not profile.exists():
        user_profile = Profile.objects.create(user=current_user, tests_taken=0)
        context['user_profile'] = user_profile 
        return render(request, 'backend/profile.html', {})

    user_profile = Profile.objects.filter(user = current_user)[0]
    heart_patient_array = HeartPatient.objects.all().filter(user_profile=user_profile)

    cholesterol_array = []
    blood_pressure_array = []
    date_array = []
    for record in heart_patient_array:
        cholesterol_array.append(record.cholesterol)
        blood_pressure_array.append(record.resting_blood_pressure)
        date_array.append(record.date.date())
        print(record.date.date())

    context['user_profile'] = user_profile   
    context['cholesterol_array'] = cholesterol_array
    context['blood_pressure_array'] = blood_pressure_array 
    context['date_array'] = date_array
    
    return render(request, 'backend/profile.html', context)

@login_required
def consult_doctors(request):
  
    current_user = request.user

    def testDone(arr):
        for obj in arr:
            if obj.user == current_user:
                return True
        return False
  
    heartTestDone = testDone(HeartPatient.objects.all())
    diabetesTestDone = testDone(DiabetesPatient.objects.all())
    liverTestDone = testDone(LiverPatient.objects.all())

    isHeartPatient = request.session.get('isHeartPatient', False)
    isDiabetesPatient = request.session.get('isDiabetesPatient', False)
    isLiverPatient = request.session.get('isLiverPatient', False)

    context = {
        'heartTestDone' : heartTestDone,
        'diabetesTestDone' : diabetesTestDone,
        'liverTestDone' : liverTestDone,
        'isHeartPatient' : isHeartPatient,
        'isDiabetesPatient' : isDiabetesPatient,
        'isLiverPatient' : isLiverPatient,
    }

    return render(request, 'backend/consult_doctors.html', context)


def analyze1(request, parameter):

    current_user = request.user
  
    heart_array = HeartPatient.objects.all().filter(user=current_user)
    diabetes_array = DiabetesPatient.objects.all().filter(user=current_user)
    liver_array = LiverPatient.objects.all().filter(user=current_user)

    def foo(arr, x):
        x_arr = []
        date_array = []
        for record in arr:     
            if x == "cholesterol":
                x_arr.append(record.cholesterol)
            elif x == "maximum_heart_rate_achieved":
                x_arr.append(record.maximum_heart_rate_achieved)
            elif x == "glucose":
                x_arr.append(record.glucose)
            elif x == "insulin":
                x_arr.append(record.insulin)
            elif x == "bilirubin":
                x_arr.append(record.total_bilirubin)
            elif x == "total_protiens":
                x_arr.append(record.total_protiens)

            date_array.append(record.date.date())

        return [x_arr, date_array]

    context = {}
    test_taken = False
    if parameter == "cholesterol":
        temp = foo(heart_array, 'cholesterol')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        list = zip(temp[0], temp[1])
        context['list'] = list
        context['value'] = 'cholesterol'
        test_taken = True
    elif parameter == "maxHeartRateAchieved":
        temp = foo(heart_array, 'maximum_heart_rate_achieved')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'maximum_heart_rate_achieved'
        test_taken = True
    elif parameter == "glucose":
        temp = foo(diabetes_array, 'glucose')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1]) 
        context['value'] = 'glucose'
        test_taken = True
    elif parameter == "insulin":
        temp = foo(diabetes_array, 'insulin')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'insulin'
        test_taken = True
    elif parameter == "bilirubin":
        temp = foo(liver_array, 'bilirubin')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'bilirubin'
        test_taken = True
    elif parameter == "total_protiens":
        temp = foo(liver_array, 'total_protiens')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'total_protiens'
        test_taken = True

    context['test_taken'] = test_taken
    print(test_taken)
    return render(request,'backend/analyze.html', context)


def about(request):
    return render(request,'backend/about.html',{'title':'About'})