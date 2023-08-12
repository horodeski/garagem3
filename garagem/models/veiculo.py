from django.db import models

from garagem.models import Cor, Modelo

class Veiculo(models.Model):
    descricao = models.CharField(max_length=100, default="")
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos",default=2, null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} {self.descricao}"
    
    class Meta:
        verbose_name = "Veículo"
