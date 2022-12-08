from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Portafolio

class PortafolioView(TemplateView):
  template_name = "administracion/index.html"