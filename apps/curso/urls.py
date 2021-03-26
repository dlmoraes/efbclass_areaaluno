from django.urls import path

from . import views

urlpatterns = [
    path('disponiveis', views.CursoDisponiveisListView.as_view(), name='cursos_disponiveis'),
    path('materiais', views.MateriaisListView.as_view(), name='materiais'),
]