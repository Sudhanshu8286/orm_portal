from django.shortcuts import render,get_object_or_404, redirect
from doctor.models import Doctors
from product.models import Products
from .models import Deal
from .forms import DealForm

# Create your views here.

def deal_details(request):
    doctors = Doctors.objects.all()
    products = Products.objects.all()

    if request.method == 'POST':
        doctor_id = request.POST.get('Doctor_Name')
        product_id = request.POST.get('Product_name')
        quintity = request.POST.get('Quantity')
        entered_by = request.POST.get('Entered_by')
        date = request.POST.get('Date')

        doctor = Doctors.objects.get(id=doctor_id)
        product = Products.objects.get(id=product_id)
        deal = Deal(
            Doctor_Name=doctor,
            Product_Name=product,
            Quantity=quintity,
            Entered_by = entered_by,
            Date = date
        )

        deal.save()
        
    context={
        'doctors':doctors,
        'products':products
    }
    
    return render(request,'deal/deal.html',context)

def update_deal(request, pk):
    obj = Deal.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = DealForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
                # return redirect('success_view')
    else:
       
        form = DealForm(instance=obj)
    
    context = {'form': form}
    return render(request, 'deal/form.html', context)


def deal_list(request):
    deals = Deal.objects.all()
    context = {'deals': deals}
    return render(request, 'deal/list.html', context)

def delete_deal(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    
    if request.method == 'POST':
        deal.delete()
        return redirect('deal_list')
    
    context = {'deal': deal}
    return render(request, 'deal/deletedeal.html', context)