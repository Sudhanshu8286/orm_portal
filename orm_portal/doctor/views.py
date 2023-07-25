from django.shortcuts import render,HttpResponseRedirect
from .forms import DoctorRegistration
from .models import Doctors

# Create your views here.

def doc_add(request):
    if request.method == 'POST':
        fm = DoctorRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = DoctorRegistration()
    else:
        fm = DoctorRegistration()
    context = {
        'form':fm 
    }
    return render(request,'doctor/add.html',context)

def doctor_list(request):
    doct = Doctors.objects.all()
    context = {'doct': doct}
    return render(request, 'doctor/doctorlist.html', context)

#This function is for edit
def update_data(request,id):
    if request.method == 'POST':
        pi = Doctors.objects.get(pk=id)
        up = DoctorRegistration(request.POST,request.FILES,instance=pi)
        if up.is_valid():
            up.save()
    else:
        pi = Doctors.objects.get(pk=id)
        up = DoctorRegistration(instance=pi)
    context = {
        'form':up
    }
    return render(request,'doctor/updatedoc.html',context)


#This function is for delete
def delete_data(request,id):
    if request.method == 'POST':
        de = Doctors.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/dashboard')