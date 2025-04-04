from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = SimpleRouter()
router.register(r'api', UserViewSets)

urlpatterns = [
    path('', include(router.urls)),
    #Este es el path para iniciar sesion <-- Requiere email y password (POST)
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'), 
    path('form/', CustomUserFormAPI.as_view(), name='user_form_api'),
]

