from django.db import models

from media.models import Image

from .autor import Autor
from .categoria import Categoria
from .editora import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="livros",
        blank=True,
        null=True,
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="editora"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")

    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.titulo
