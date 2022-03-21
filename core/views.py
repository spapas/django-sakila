from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from simple_stats import get_stats

STATS_CFG = cfg = [
    {
        'label': 'Total films',
        'kind': 'query_aggregate_single',
        'method': 'count',
        'field': 'film_id',
    },
    {
        'label': 'Per category',
        'kind': 'query_aggregate',
        'method': 'count',
        'field': 'filmcategory__category__name',
        'limit': 15,
    },
    {
        'label': 'Per Actor',
        'kind': 'query_aggregate',
        'method': 'count',
        'field': 'filmactor__actor__last_name',
        'limit': 15,
    },
    {
        'label': 'Per store',
        'kind': 'query_aggregate',
        'method': 'count',
        'field': 'inventory__store__address__address',
        'limit': 15,
    },
    {
        'label': 'Per staff',
        'kind': 'query_aggregate',
        'method': 'count',
        'field': 'inventory__rental__staff__last_name',
        'limit': 15,
    },
    {
        'label': 'Per customer',
        'kind': 'query_aggregate',
        'method': 'count',
        'field': 'inventory__rental__customer__last_name',
        'limit': 15,
    },
 

]

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = models.Film.objects.all()
        
        stats = get_stats(qs, STATS_CFG)
        ctx['stats'] = stats
        return ctx