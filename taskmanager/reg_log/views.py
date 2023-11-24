from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form import LoginForm, RegistrationForm

def home(request):
    return render(request, 'reg_log/Aboutus.html')

def registration(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = 'Error 404'
    else:
        form = RegistrationForm()
    context = {
       'form': form,
       'error': error
    }
    return render(request, 'reg_log/Registration.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Incorrect password or username')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'reg_log/Login.html', context)