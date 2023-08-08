from django.shortcuts import render, redirect
from .models import ContactInfo


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
        return redirect('home')
    return render(request, 'website/index.html')



