from django.urls import path
from departments import views

urlpatterns = [

    path('', views.DepartmentCreateView.as_view(), name='cr_dp'),


    
]