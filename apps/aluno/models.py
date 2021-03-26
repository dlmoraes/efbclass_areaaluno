from django.db import models

from apps.core.models import Timestamps
from apps.curso.models import Topico
from apps.core.lists import TIPO_USER, STATUS_CHOICES


class Empresa(Timestamps):
    nome = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Regional(Timestamps):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Regional'
        verbose_name_plural = 'Regionais'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Departamento(Timestamps):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Setor(Timestamps):
    nome = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Equipe(Timestamps):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Aluno(Timestamps):
    matricula = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    nome = models.CharField(max_length=150)
    dta_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    foto_perfil = models.CharField(max_length=200, blank=True)
    tipo_acesso = models.IntegerField(choices=TIPO_USER, default=1)
    cod_ativacao = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class GrupoTurma(models.Model):
    nome = models.CharField(max_length=60)
    membros = models.ManyToManyField(Aluno, through='Turma')

    def __str__(self):
        return self.nome


class Turma(Timestamps):
    equipes = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    alunos = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoTurma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['equipes', 'alunos']


class Discussao(Timestamps):
    dicussao_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Discussão'
        verbose_name_plural = 'Discussões'
        ordering = ['titulo']


class Comentario(Timestamps):
    comenta_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    mensagem = models.TextField()

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['comenta_aluno']


class MovTeste(Timestamps):
    alunos = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    topicos = models.ForeignKey(Topico, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    ultima_posicao = models.CharField(max_length=30, blank=True)
    ultima_questao = models.CharField(max_length=30, blank=True)
