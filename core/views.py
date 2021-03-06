from rest_framework.viewsets import ModelViewSet
from core.models import Autor, Categoria, Livro
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, AutorSerializer
from core.models import Editora

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer