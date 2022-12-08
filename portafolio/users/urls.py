from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
  path('accounts/login/', LoginView.as_view(), name="login"),
  path('logout/', logout_then_login, name='logout')
]