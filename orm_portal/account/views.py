
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from appointment.views import appointment_list
from product.views import add
from dashboard.views import dashboard_view
from .forms import RegistrationForm
# from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'base/register.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            return redirect(dashboard_view)
        
        else:
            return render(request,'base/register.html',{'form_data':form})
        
    return render(request,'base/register.html',{'form_data':form})




class MyLoginView(LoginView):
    

    def form_valid(self, form):
        user = form.get_user()

        if user is not None:
            self.request.session.set_expiry(0)  # Optional: Set session expiry time
            return redirect('dashboard')  # Redirect to the dashboard or desired page upon successful login
            return render(request, 'account/login.html', context)
        
        error_message = 'Invalid username or password. Please try again.'
        context = self.get_context_data(form=form)
        context['error_message'] = error_message
        return self.render_to_response(context)
    
def MyLogoutView(request):
    logout(request)
    return redirect('/') 

