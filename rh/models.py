from django.db import models
from django.utils import timezone

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

class Produtos(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.CharField(max_length= 100)
    categoria = models.CharField(max_length=100,null=True, blank=True)
    em_estoque = models.BooleanField(default= True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
    
class Carrinhos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=11)
    cpf = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def __str__(self):
        return f"{self.nome} - {self.email} ({self.tel}) ({self.cpf}) ({self.endereco})"
