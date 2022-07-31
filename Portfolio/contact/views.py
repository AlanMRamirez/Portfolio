from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            phone_number = request.POST.get('phone_number', '')
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "Portfolio: New message",
                "From {} <{}> and phone number: {}\n\nHe Write s\n\n{}".format(name, email, phone_number, content),
                settings.EMAIL_HOST_USER,
                ["alanmondragonramirez19@gmail.com"],
                reply_to=[email]
            )
            try:
                #Todo ha salido bien, redireccionamos a OK
                email.send()
                return redirect(reverse('contact:contact')+"?send")
            except:
                #Algo no ha salido bien, redireccionamos a FAIL
                return redirect(reverse('contact:contact')+"?fail")
    
    return render(request, 'contact/contact.html',{
        'form': contact_form
    })
