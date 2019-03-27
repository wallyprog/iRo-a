from django.db import models
from django.core.validators import MinValueValidator
from django.utils.datetime_safe import datetime
# Create your models here.

class agricutor(models.Model):
    nome = models.CharField(max_length=50, null=False)
    idade = models.IntegerField(null=False)
    produtos = models.TextField()
class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=500,null=False)
    quantidade = models.IntegerField(null=False)
    data_colheita = models.DateTimeField(default=datetime.now(),null=False)
class feirante(models.Model):
    nome = models.CharField(max_length=50, null=False)
    idade = models.IntegerField(null=False)
    