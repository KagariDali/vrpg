from django.db import models

# Cria suas classes
class Campus(models.Model): 
    # Definir os atributos
    nome = models.CharField(max_length=100)

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    # Se quiser apagar tudo, faz um efeito cascata com todas as ligações. Utilize Cascate ao invés de protec.

class TipoSolivitacao(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    prazo_externo = models.CharField(max_length=250)
    prazo_externo_dias = models.PositiveSmallIntegerField(defalt=0)
    prazo_interno = models.CharField(max_length=250)
    prazo_interno_dias = models.PositiveSmallIntegerField(default=0)
    concluido = models.BooleanField(default = false )
