from django.db import models

# Suas classes
class Bot(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    categoria = categoria
    link = models.CharField(max_length=255)
    cadastro_em = models.DateField(auto_now = True)

class categoria(models.Model):
    nome = models.CharField(max_length=150)

class Avaliacao(models.Model):
    nota = models.IntegerField(DecimalField = 1, MaxValueValidator = 10,  MinValueValidator = 0.0)
    bot = Bot
    data_hora = models.DateField(auto_now = True)

class Comentario(models.Model):
    comentario = models.TextField()
    data_hora = models.DateField(auto_now = True)
    bot = Bot
