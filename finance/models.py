from django.db import models

class finance(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, blank=False)
    email = models.EmailField(blank=False)
    valor = models.FloatField(blank=False)
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    categoria = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome