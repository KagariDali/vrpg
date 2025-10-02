from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagem = models.ImageField(upload_to='usuarios_imagens/', blank=True, null=True)

    def __str__(self):
        return self.usuario.username

# Suas classes

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Bot(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    link = models.URLField(max_length=255)
    cadastro_em = models.DateTimeField(auto_now_add = True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    imagem = models.ImageField(upload_to='bots_imagens/', blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    nota = models.PositiveSmallIntegerField(default=5)
    bot = models.ForeignKey(Bot, on_delete=models.PROTECT)
    data_hora = models.DateField(auto_now_add = True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nota


class Comentario(models.Model):
    comentario = models.TextField()
    data_hora = models.DateTimeField(auto_now_add = True)
    bot = models.ForeignKey(Bot, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.comentario
