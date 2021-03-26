from django.db import models

from apps.core.models import Timestamps
from apps.core.lists import NIVEIS_CHOICES


class Categoria(Timestamps):
    nome = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class TipoMaterial(Timestamps):
    nome = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Tipo de Material'
        verbose_name_plural = 'Tipos de Material'

    def __str__(self):
        return self.nome


class Curso(Timestamps):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200, blank=True)
    nivel = models.IntegerField(choices=NIVEIS_CHOICES, default=1)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Material(Timestamps):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    material_nome = models.CharField(max_length=120)
    material_conteudo = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering = ['material_nome']

    def __str__(self):
        return self.material_nome


class Topico(Timestamps):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    sessao = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class SubTopico(Timestamps):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    subtopico_num = models.IntegerField()

    def __str__(self):
        return self.titulo


class Aula(Timestamps):
    subtopico = models.ForeignKey(SubTopico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    numero = models.IntegerField()

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Questionario(Timestamps):
    subtopico = models.ForeignKey(SubTopico, on_delete=models.CASCADE)
    questao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
        ordering = ['questao']

    def __str__(self):
        return self.questao


class Resposta(Timestamps):
    questao_resp = models.OneToOneField(Questionario, on_delete=models.CASCADE, parent_link=True)
    resposta = models.CharField(max_length=255)
    flag = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['resposta']

    def __str__(self):
        return self.resposta
