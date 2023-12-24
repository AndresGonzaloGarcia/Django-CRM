from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addRecordForm
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
        messages.success(request, "Tenes que iniciar sesion para ver la informacion.")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id= pk)
        delete_it.delete()
        messages.success(request, "Los datos han sido eliminados correctamente. ")
        return redirect('home')
    else:
        messages.success(request, "Tenes que iniciar sesion para eliminar los datos... ")
        return redirect('home')
    
def add_record(request):
    form = addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Datos agregados.')
                return redirect('home')

        return render(request, 'add_record.html', {'form': form })
    else:
        messages.success(request, 'Tenes que iniciar sesion para agregar datos...')
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id= pk)
        form = addRecordForm(request.POST or None, instance= current_record) #instance toma el record que ya teniamos y lo pasa directamente a addRecord
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos actualizados.')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form })
    else:
        messages.success(request, 'Tenes que iniciar sesion para modificar datos...')
        return redirect('home')







        
