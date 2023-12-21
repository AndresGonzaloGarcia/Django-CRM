from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all() #toma todo lo de la tabla y lo asigna a esta var.
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autenticar
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Iniciaste sesion correctamente, bienvenido!')
            return redirect('home')
        else:
            messages.success(request, 'Hubo un error mientras intentaste acceder, por favor intenta nuevamente :/')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records}) 
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Cerraste tu sesion, hasta pronto!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Te registraste con exito <3")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #buscar records
        customer_record = Record.objects.get(id= pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Tenes que estar registrado para ver la informacion.")
        return redirect('home')

        
