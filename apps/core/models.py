from django.db import models


class Timestamps(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FAQ(Timestamps):
    faq_pergunta = models.CharField(max_length=200)
    faq_resposta = models.TextField()
