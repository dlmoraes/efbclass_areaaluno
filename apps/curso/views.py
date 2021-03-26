from django.views.generic import TemplateView, ListView, DetailView
from .models import Curso, Material


class CursoDisponiveisListView(ListView):
    template_name = 'cursos_disponiveis.html'
    model = Curso

    def get_queryset(self):
        return super(CursoDisponiveisListView, self).get_queryset().select_related('categoria')


class MateriaisListView(ListView):
    template_name = 'materiais.html'
    model = Material

    def get_queryset(self):
        return super(MateriaisListView, self).get_queryset().select_related('curso', 'tipo')
