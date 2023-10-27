from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .form import ContactForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')


def list(request):
    contacts = Contact.objects.all()
    return render(request,'contacts/list.html',{'contacts':contacts})


def addContact(request):
    formulario = ContactForm(request.POST or None,request.FILES or 
    None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,  "¡ El contacto fue creado correctamente !")
        return redirect('lista')
    return render(request,'contacts/add.html',{'formulario':formulario})


def editContact(request,id):
    contact = Contact.objects.get(id=id)
    formulario = ContactForm(request.POST or None,request.FILES or None ,instance=contact)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        messages.success(request, "¡ El contacto fue ha actualizado correctamente !")
        return redirect('lista')
    return render(request,'contacts/update.html',{'formulario':formulario})

def deleteContact(request,id):
    contact = Contact.objects.get(id=id) 
    contact.delete()
    messages.success(request, "¡ El contacto fue ha eliminado correctamente !")
    return redirect('lista')



