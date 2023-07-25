from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductRegistration
from .models import Products

# Create your views here.

#This function is for add and view all products
def add(request):
    if request.method == 'POST':
        fm = ProductRegistration(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = ProductRegistration()
    else:
        fm = ProductRegistration()
    context = {
        'form':fm ,
    }
    return render(request,'product/add.html',context)

#This function is for edit
def update_data(request,id):
    if request.method == 'POST':
        pi = Products.objects.get(pk=id)
        up = ProductRegistration(request.POST,request.FILES,instance=pi)
        if up.is_valid():
            up.save()
    else:
        pi = Products.objects.get(pk=id)
        up = ProductRegistration(instance=pi)
    context = {
        'form':up
    }
    return render(request,'product/updateproduct.html',context)

def product_list(request):
    prod = Products.objects.all()
    context = {'prod': prod}
    return render(request, 'product/productlist.html', context)

#This function is for delete
def delete_data(request,id):
    if request.method == 'POST':
        de = Products.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/dashboard')

