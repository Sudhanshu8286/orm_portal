from django.shortcuts import render
from django.db.models import Count
from product.models import Products
from appointment.models import Appointment
from deal.models import Deal
from .forms import DealsForm,ProductForm,DoctorForm,DealsForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from account.forms import RegistrationForm



# Create your views here.
class EmployeeListView(ListView):
    model = User
    template_name = 'superuser/employee.html'
    context_object_name = 'super'

def productview(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            
            
            prodata = Products.objects.filter(EnteredBy=employee)
            
            return render(request, 'superuser/products.html', {'prodata': prodata, 'emp':employee.username})

    else:
        form = ProductForm()

    return render(request, 'superuser/productform.html', {'form': form})


def doctorview(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            visits_data = Appointment.objects.filter( Entered_by=employee, Date_of_Schedule__month=month).values('Entered_by').annotate(total_appointments=Count('id'))
            
            return render(request, 'superuser/doctor.html', {'visits_data': visits_data,'emp':employee.username })

    else:
        form = DoctorForm()

    return render(request, 'superuser/doctorform.html', {'form': form})


def dealsview(request):
    if request.method == 'POST':
        form = DealsForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            deals_data = Deal.objects.filter(Entered_by=employee, Date__month=month).values('Entered_by').annotate(total_deals=Count('id'))
            
            return render(request, 'superuser/deals.html', {'deals_data': deals_data, 'emp':employee.username})

    else:
        form = DealsForm()

    return render(request, 'superuser/dealform.html', {'form': form})

