from django.shortcuts import render, redirect
from .models import ContactInfo
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactInfo.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, 'Thank you for reaching out, we will be in touch!')
        return redirect('home')
    return render(request, 'website/index.html')



