from django.shortcuts import render, redirect
from .models import ContactInfo
from django.contrib import messages


def index(request):
    return render(request, 'website/index.html')


def services(request):
    return render(request, 'website/services.html')


def blog(request):
    return render(request, 'website/blog.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        return redirect('website:thank-you')

    return render(request, 'website/contact.html')


def thankyou_page(request):
    return render(request, 'website/thank-you.html')
