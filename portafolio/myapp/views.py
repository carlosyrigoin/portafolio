from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Portafolio

class PortafolioView(TemplateView):
    template_name = "administracion/portafolio.html"

class AdministracionView(LoginRequiredMixin, TemplateView):
    template_name = "administracion/index.html"
    