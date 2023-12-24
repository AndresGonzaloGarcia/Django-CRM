from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requisitos. 150 carácteres o menos. Letras, números y @/./+/-/_ solamente.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser muy similar a tus datos personales. </li><li>Tu contraseña debe tener al menos 8 caracteres. </li><li>Tu contraseña no debe ser muy común. </li><li>Tu contraseña no puede ser enteramente numérica. </li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Para verificar, ingrese la misma contraseña ingresada anteriormente. </small></span>'	


class addRecordForm(forms.ModelForm):
    first_name= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    mail= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    phone= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}))
    address= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}))
    city= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}))
    state= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provincia'}))
    zipcode= forms.CharField(required= True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Codigo Postal'}))

    class Meta:
        model = Record
        exclude = ('user',)