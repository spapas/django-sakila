from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        films = models.Film.objects.all()
        ctx['films'] = films
        return ctx