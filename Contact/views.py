from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_page(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_page')

    return render(request, 'contact/contact.html')
