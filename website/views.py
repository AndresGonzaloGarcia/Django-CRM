from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autenticar
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in succesfully.')
            return redirect('home')
        else:
            messages.success(request, 'There was an error while trying to log in, please try again. :/')
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out succesfully.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #autentica y guarda
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(authenticate(request, username=username, password=password))
            login(request, user)
            messages.success(request, "You hace registered succesfully <3")
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form': form})