"""
URL configuration for health_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from product import views
from django.conf.urls.static import static
from django.conf import settings
from account.views import register
from account.views import MyLoginView
from account.views import MyLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.add,name='add'),
    path('product_list/', views.product_list, name='product_list'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
    path('',include('doctor.urls')),
    path('deletedatadoc',include('doctor.urls')),
    path('updatedatadoc',include('doctor.urls')),
    path('',include('appointment.urls')),
    path('',include('deal.urls')),
    path('delete_deal',include('deal.urls')),
    path('update_deal',include('deal.urls')),
    path('',MyLoginView.as_view(template_name='base/login.html'),name='login'),
    path('',MyLogoutView,name='logout'),
    path('',include('dashboard.urls')),
    path('',include('superuser.urls')),
    path('register/',register,name='register-page'),
]

if settings:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)