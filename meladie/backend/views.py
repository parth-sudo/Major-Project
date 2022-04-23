from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def home(request):
    return render(request, 'backend/home.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'The account for {username} has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'backend/register.html', {'form':form})


def about(request):
    return render(request,'backend/about.html',{'title':'About'})