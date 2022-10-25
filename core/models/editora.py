from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
