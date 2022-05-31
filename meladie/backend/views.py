from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, HeartPatientForm, DiabetesPatientForm, LiverPatientForm
from django.contrib.auth.models import User
from .models import BookDoctorAppointment, Doctor, Profile, HeartPatient, DiabetesPatient, Disease, LiverPatient, BookLabTest
from .predictions import heart_disease, diabetes, liver_disease
from django.core.mail import send_mail
from django.conf import settings
from .extras import current_milli_time, heart_parameters_info, diabetes_parameters_info, liver_parameters_info, get_city, slot_split
import datetime

def home(request):

    appointments = BookDoctorAppointment.objects.all()
    today = str(datetime.date.today())
    day = today.split('-')[2]
    day_today = int(day)

    oldAppointments = []
    for app in appointments:
        date = str(app.time_of_creation)
        date_of_creation = date.split(' ')[0]
        day_of_creation = int(date_of_creation.split('-')[2])

        if day_today - day_of_creation >= 1:
            oldAppointments.append(app)
    
    for app in oldAppointments:
        BookDoctorAppointment.objects.filter(time_of_creation=app.time_of_creation).delete()

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
    chest_pain_type = {
      "Typical Angina" : "Substernal chest discomfort of characteristic quality and duration, Provoked by exertion or emotional stress, Relieved by rest and/ or GTN", 
                 "Atypical Angina" : "Meets two of above mentioned characteristics", 
                 "Non-Anginal Pain" : "Meets one or none of the characteristics"
    }

    context['chest_pain_type'] = chest_pain_type
    context['parameters_info'] = heart_parameters_info
    context['disease_name'] = "Heart Disease"
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
            serum_cholesterol=form.cleaned_data.get('serum_cholesterol')
            fasting_blood_sugar = form.cleaned_data.get('fasting_blood_sugar_greater_than_120')
            resting_electrocardiographic_results = form.cleaned_data.get('resting_electrocardiographic_results')
            exercise_induced_angina = form.cleaned_data.get('exercise_induced_angina')
            old_peak=form.cleaned_data.get('old_peak')
            slope = form.cleaned_data.get('slope')
            number_of_major_vessels_coloured_by_flouroscopy = form.cleaned_data.get('number_of_major_vessels_coloured_by_flouroscopy')

            result = heart_disease(age, sex, chest_pain_type, resting_blood_pressure, serum_cholesterol, fasting_blood_sugar, resting_electrocardiographic_results, exercise_induced_angina, old_peak, slope, number_of_major_vessels_coloured_by_flouroscopy)
        
            request.session['isHeartPatient'] = True if result == 1 else False

            answer = "Heart Disease detected." if result == 1 else "No, you don't have heart disease."
            context['answer'] = answer
            context['disease_name'] = "Heart Disease"
            # context['chest_pain_type'] = chest_pain_type
            context['disease_detected'] = True if result == 1 else False
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = HeartPatientForm()
        context['form'] = form
        context['answer'] = ""
        context['disease_detected'] = False
        # context['chest_pain_type'] = chest_pain_type
    return render(request,'backend/disease_prediction.html', context)

@login_required
def diabetes_prediction(request):
    context = {}

    context['parameters_info'] = diabetes_parameters_info
    context['disease_name'] = "Diabetes"
    if request.method == 'POST':
        form = DiabetesPatientForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            context['form'] = form
            glucose=form.cleaned_data.get('glucose')
            blood_pressure=form.cleaned_data.get('blood_pressure')
            insulin=form.cleaned_data.get('insulin')
            body_mass_index=form.cleaned_data.get('body_mass_index')
            age=form.cleaned_data.get('age')

            result = diabetes(glucose, blood_pressure, insulin, body_mass_index, age)
       
            request.session['isDiabetesPatient'] = True if result == 1 else False
            answer = "Diabetes detected." if result == 1 else "You don't have diabetes."
            context['answer'] = answer
            context['disease_detected'] = True if result == 1 else False
            context['disease_name'] = "Diabetes"
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = DiabetesPatientForm()
        context['form'] = form
        context['answer'] = ""
        context['disease_detected'] = False
    return render(request,'backend/disease_prediction.html', context)

@login_required
def liver_prediction(request):
    context = {}
   
    context['parameters_info'] = liver_parameters_info
    context['disease_name'] = "Liver Disease"

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

            answer = "Liver Disease detected." if result == 1 else "No, you don't liver disease."
            context['answer'] = answer
            context['disease_name'] = "Liver Disease"
            context['disease_detected'] = True if result == 1 else False
          
            return render(request, 'backend/disease_prediction.html', context)
    else:
        form = LiverPatientForm()
        context['form'] = form
        context['answer'] = ""
        context['disease_detected'] = False
    return render(request,'backend/disease_prediction.html', context)

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
        user_profile = Profile.objects.create(user=current_user)
        context['user_profile'] = user_profile 
        return render(request, 'backend/profile.html', {})

    user_profile = Profile.objects.filter(user = current_user)[0]
    heart_patient_array = HeartPatient.objects.all().filter(user=current_user)
    liver_patient_array = LiverPatient.objects.all().filter(user=current_user)
    diabetes_patient_array = DiabetesPatient.objects.all().filter(user=current_user)

    count = 0
    context['heart_test'] = ""
    context['liver_test'] = ""
    context['diabetes_test'] = ""
    if heart_patient_array.exists():
        context['heart_test'] = ' Heart Disease(s) Prediction Test'
        count += 1
    if liver_patient_array.exists():
        context['liver_test'] = ', Liver Disease(s) Prediction Test'
        count += 1
    if diabetes_patient_array.exists():
        context['diabetes_test'] = ', Diabetes Prediction Test'
        count += 1

    context['count'] = count
    context['user_profile'] = user_profile   
   
    
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

    city = get_city()

    heart_doctors = Doctor.objects.all().filter(specialization=1, city = city)
    diabetes_doctors = Doctor.objects.all().filter(specialization=2, city = city)
    liver_doctors = Doctor.objects.all().filter(specialization=3, city = city)
    

    context = {
        'heartTestDone' : heartTestDone,
        'diabetesTestDone' : diabetesTestDone,
        'liverTestDone' : liverTestDone,
        'isHeartPatient' : isHeartPatient,
        'isDiabetesPatient' : isDiabetesPatient,
        'isLiverPatient' : isLiverPatient,
        'heart_doctors' : heart_doctors,
        'diabetes_doctors' : diabetes_doctors,
        'liver_doctors' : liver_doctors,
    }

    return render(request, 'backend/consult_doctors.html', context)

@login_required
def analyze1(request, parameter):

    current_user = request.user
  
    heart_array = HeartPatient.objects.all().filter(user=current_user)
    diabetes_array = DiabetesPatient.objects.all().filter(user=current_user)
    liver_array = LiverPatient.objects.all().filter(user=current_user)

    def foo(arr, x):
        x_arr = []
        date_array = []
        for record in arr:     
            if x == "serum_cholesterol":
                x_arr.append(record.serum_cholesterol)
            elif x == "resting_blood_pressure":
                x_arr.append(record.resting_blood_pressure)
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
        temp = foo(heart_array, 'serum_cholesterol')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        list = zip(temp[0], temp[1])
        context['list'] = list
        context['value'] = 'serum_cholesterol'
        context['heading'] = 'Serum Cholesterol'
        test_taken = True
    elif parameter == "restingBloodPressure":
        temp = foo(heart_array, 'resting_blood_pressure')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'resting_blood_pressure'
        context['heading'] = 'Resting Blood Pressure'
        test_taken = True
    elif parameter == "glucose":
        temp = foo(diabetes_array, 'glucose')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1]) 
        context['value'] = 'glucose'
        context['heading'] = 'Glucose'
        test_taken = True
    elif parameter == "insulin":
        temp = foo(diabetes_array, 'insulin')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'insulin'
        context['heading'] = 'Insulin'
        test_taken = True
    elif parameter == "bilirubin":
        temp = foo(liver_array, 'bilirubin')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'bilirubin'
        context['heading'] = 'Total Bilirubin'
        test_taken = True
    elif parameter == "total_protiens":
        temp = foo(liver_array, 'total_protiens')
        context['value_array'] = temp[0]
        context['date_array'] = temp[1]
        context['list'] = zip(temp[0], temp[1])
        context['value'] = 'total_protiens'
        context['heading'] = 'Total Protiens'
        test_taken = True

    context['test_taken'] = test_taken
    print(test_taken)
    return render(request,'backend/analyze.html', context)


def about(request):
    return render(request,'backend/about.html',{'title':'About'})


@login_required
def book_lab_test(request):
    context = {}
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        test_name = request.POST.get('testName')
      
        # test1 = request.POST.get('test1')
        date = request.POST.get('date')
        time_slot = request.POST.get('timeSlot')
        print(date)

        prof = BookLabTest.objects.create(full_name=full_name,address=address,contact=contact,test_name=test_name,time_slot=time_slot,date=date)

        # send email function.
        email_receiver = request.user.email
        email_sender = settings.EMAIL_HOST_USER
        context = {'full_name':full_name,'test_name':test_name,'time_slot':time_slot,'email':email_receiver}
        
        msg = f"Dear {full_name}, your test has been booked successfully. The practioner will arrive at somewhere between {time_slot} on {date}."
        send_mail("Test Confirmation Email", msg, email_sender, [email_receiver])
        context['booked'] = prof

        return render(request, 'backend/book_lab_test.html', context)

    return render(request, 'backend/book_lab_test.html', {})

def book_doctor_appointment(request, doctor_name):
    context = {}
    # array of time strings (arrTS) = breakdown function.
    # objectArr = used up time slots.
    # 
    doc = Doctor.objects.filter(full_name=doctor_name).first()

    timeStringArr = doc.availability.split('-')
 
    actualTimeArr = slot_split(timeStringArr[0], timeStringArr[1])
  
    availability = []
    for timeSlot in actualTimeArr:
        slot = BookDoctorAppointment.objects.filter(time_slot=timeSlot).first()
        if slot == None:
            availability.append(timeSlot)

    context['available_time_slots'] = availability
    if request.method == "POST":
        time_slot = request.POST.get('timeSlot')
        date = request.POST.get('date')

        doc = Doctor.objects.filter(full_name=doctor_name).first()
        address = doc.address
        contact = doc.contact
        email_receiver = request.user.email
        email_sender = settings.EMAIL_HOST_USER
        # context = {'full_name':full_name,'test_name':test_name,'time_slot':time_slot,'email':email_receiver}
        proof = BookDoctorAppointment.objects.create(user=request.user, time_slot=time_slot, date=date)
     
        msg = f"Dear {request.user.username}, your appointment with {doc.full_name} has been booked successfully. Reach the address- {address} sometime between {time_slot} on {date}. Contact {contact} in case of any issue."
   
        send_mail("Appointment Confirmation Email", msg, email_sender, [email_receiver])
        
        context['booked'] = proof

        return render(request, 'backend/book_doctor_appointment.html', context)

    return render(request,'backend/book_doctor_appointment.html',context)