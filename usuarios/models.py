from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome