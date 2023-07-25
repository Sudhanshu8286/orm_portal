
from django.urls import path

from . import views

urlpatterns = [
    path('docadd',views.doc_add,name='docadd'),
    path('delete/<int:id>/',views.delete_data,name='deletedatadoc'),
    path('<int:id>/',views.update_data,name='updatedatadoc'),
    path('doctor_list',views.doctor_list,name='doctor_list'),
]

