
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api.Views.changePasswordView import PasswordTokenCheckAPI
from api.Views.changePasswordView import RequestPasswordResetEmail, SetNewPasswordAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('auth/', obtain_auth_token),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]
