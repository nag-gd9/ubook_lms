from django.urls import path
from adminstartion import views

urlpatterns = [

    path('create-student/', views.create_student, name='cs'),
    path('create-professor/', views.create_professor, name='cp'),
    path('create-lower-staff/', views.create_admin, name='ca'),
    # path('add-student/', add_student_form_view, name='add_student'),

    
]