from django.urls import path
from  .import views
from .views import EmployeeListView


urlpatterns = [
    path('doctorview/', views.doctorview, name='doctorview'),
    path('dealsview/', views.dealsview, name='dealsview'),
    path('emplist/', EmployeeListView.as_view(), name='emplist'),
    path('productview/', views.productview, name='productview'),
]
