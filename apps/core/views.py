from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplate(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomeTemplate, self).get_context_data(**kwargs)
        data['cartoes_resumo_data'] = [
            {
                'valor': 5,
                'descricao': 'Aulas',
                'icone': 'ion ion-bag',
                'cor': 'bg-success'
            },
            {
                'valor': 4,
                'descricao': 'Provas',
                'icone': 'ion ion-stats-bars',
                'cor': 'bg-info'
            },
            {
                'valor': 10,
                'descricao': 'Questões Resolvidas',
                'icone': 'ion ion-bookmark',
                'cor': 'bg-warning'
            },
            {
                'valor': 10,
                'descricao': 'Questões Resolvidas',
                'icone': 'ion ion-alert',
                'cor': 'bg-danger'
            }
        ]
        return data