from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Categoria, Cor, Veiculo, Acessorio, Modelo
from garagem.serializers import (
    MarcaSerializer,
    CategoriaSerializer,
    CorSerializer,
    ModeloSerializer,
    VeiculoSerializer,
    VeiculoListSerializer,
    VeiculoDetailSerializer,
    AcessorioSerializer,
)


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_classes = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, VeiculoSerializer)
