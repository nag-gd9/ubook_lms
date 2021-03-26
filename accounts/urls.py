from django.urls import path, include
from accounts import views



urlpatterns = [
    # web login urls
    path('login/', views.login_registration_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
