from django.urls import path, re_path
from home.views import home_view, add_student_form_view, list_student_view, perm, StudentView, StudentUpdateView

urlpatterns = [
    path('', home_view, name='home'),
    path('add-student/', add_student_form_view, name='add_student'),
    path('list-students/', list_student_view, name='list_students'),
    path('perm/', perm ),
    path('<str:id>/student/', StudentUpdateView.as_view(), name='update-student'),
    re_path('student-form/(?P<id>[0-9])/$', StudentUpdateView.as_view()),
] 