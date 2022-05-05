from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from .models import Profile

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
def disease_prediction(request):
    #todo
    return render(request,'backend/disease_prediction.html', {})

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