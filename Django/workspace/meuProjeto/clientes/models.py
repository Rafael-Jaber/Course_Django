from django.db import models



class Cliente(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.cliente.nome + ' - ' + self.descricao + ' - ' + self.numero
