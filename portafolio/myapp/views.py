from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Portafolio
from .forms import PortafolioForm

class PortafolioView(TemplateView):
    template_name = "administracion/portafolio.html"

class AdministracionView(LoginRequiredMixin, TemplateView):
    template_name = "administracion/index.html"

class PortafolioCreate(LoginRequiredMixin, FormView):
    model = Portafolio
    template_name = "administracion/create.html"
    form_class = PortafolioForm

    def form_valid(self, form):
        Portafolio.objects.create(**form.cleaned_data)
        return redirect("administracion")


@login_required
def deleteClassRoom(request, id):
    portafolio = Portafolio.objects.get(id=id)
    portafolio.delete()
    return redirect("administracion")