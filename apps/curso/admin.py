from django.contrib import admin

from . import models


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TipoMaterial)
class TipoMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Topico)
class TopicoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubTopico)
class SubTopicoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Resposta)
class RespostaAdmin(admin.ModelAdmin):
    pass
