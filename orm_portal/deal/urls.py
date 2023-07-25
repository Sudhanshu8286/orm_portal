from django.urls import path
from . import views
from .views import deal_list,delete_deal,update_deal

urlpatterns = [
    path('deal/',views.deal_details,name='deal'),
    path('deal_list/', deal_list, name='deal_list'),
    path('delete/<int:pk>', delete_deal, name='delete_deal'),
    path('update/<int:pk>/', update_deal, name='update_deal'),

]