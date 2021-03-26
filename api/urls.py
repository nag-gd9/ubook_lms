from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from knox import views as knox_views
from api.views import LoginView, CreateUserAPI, EmpView, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'emp', EmpView)


urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('knox.urls')),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register/', CreateUserAPI.as_view(), name='knox_register'),
    
]