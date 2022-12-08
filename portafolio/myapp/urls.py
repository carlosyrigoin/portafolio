from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
  path('', views.PortafolioView.as_view(), name="index")
]