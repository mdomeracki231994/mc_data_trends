from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'cms/index.html')


def add_sales_leads(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        company_address_line_1 = request.POST.get('company_address_line_1')
        company_address_line_2 = request.POST.get('company_address_line_2')
        company_city = request.POST.get('company_city')
        company_state = request.POST.get('company_state')
        company_zip = request.POST.get('company_zip')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        customer_type = request.POST.get('customer_type')
        source_of_lead = request.POST.get('source_of_lead')
        notes = request.POST.get('notes')

        # Perform data validation if needed

        # Create a SalesLead instance and save it
        SalesLead.objects.create(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            company_address_line_1=company_address_line_1,
            company_address_line_2=company_address_line_2,
            company_city=company_city,
            company_state=company_state,
            company_zip=company_zip,
            phone_number=phone_number,
            email=email,
            customer_type=customer_type,
            source_of_lead=source_of_lead,
            notes=notes
        )

    return render(request, 'cms/add_sales_leads.html')


def sales_lead_index(request):
    sales_leads = SalesLead.objects.all()
    context = {
        'sales_leads': sales_leads,
    }
    return render(request, 'cms/sales_lead_index.html', context)
