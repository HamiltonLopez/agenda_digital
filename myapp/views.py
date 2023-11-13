from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'index.html')


def list(request):
    contacts = Contact.objects.all()
    return render(request,'contacts/list.html',{'contacts':contacts, 'filtro': ''})


def filtrar(request):
    filtro = request.GET.get('search', '').lower()
    contacts = Contact.objects.filter( Q(name__icontains=filtro) | Q(phone__icontains=filtro) ) 
    return render(request,'contacts/list.html', {'contacts':contacts, 'filtro': filtro})

def addContact(request):
    formulario = ContactForm(request.POST or None,request.FILES or 
    None)
    if formulario.is_valid():
        numero = request.POST.get('phone', '')
        try:
            numero_entero = int(numero)
            resultado = f"El número ingresado es {numero_entero}"
            formulario.save()
            messages.success(request,  "¡ El contacto fue creado correctamente !")
            return redirect('lista')
        except ValueError:
            messages.success(request,  "¡ Debe ingresar un número válido !")
            return redirect('agregar')    
        
    return render(request,'contacts/add.html',{'formulario':formulario})


def editContact(request,id):
    contact = Contact.objects.get(id=id)
    formulario = ContactForm(request.POST or None,request.FILES or None ,instance=contact)
    if formulario.is_valid() and request.method == 'POST':
        numero = request.POST.get('phone','')
        print(numero)
        try:
            numero_entero = int(numero)
            formulario.save()
            messages.success(request, "¡ El contacto fue ha actualizado correctamente !")
            return redirect('lista')
        except ValueError:
            messages.success(request,  "¡ Debe ingresar un número válido !")
            return redirect(reverse('editar', args=[id]))
    return render(request,'contacts/update.html',{'formulario':formulario})

def deleteContact(request,id):
    contact = Contact.objects.get(id=id) 
    contact.delete()
    messages.success(request, "¡ El contacto fue ha eliminado correctamente !")
    return redirect('lista')



