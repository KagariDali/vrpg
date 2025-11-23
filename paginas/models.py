from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import io
from django.core.files.base import ContentFile

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagem = models.ImageField(upload_to='usuarios_imagens/', blank=True, null=True)

    def __str__(self):
        return self.usuario.username

    def save(self, *args, **kwargs):
        # Processa e normaliza a imagem de perfil (converte para JPEG e redimensiona)
        try:
            if self.imagem and hasattr(self.imagem, 'file'):
                self.imagem.open()
                img = Image.open(self.imagem)
                # força conversão para RGB (evita problemas com PNG/CMYK)
                img = img.convert('RGB')
                max_size = (500, 500)
                resample = getattr(Image, 'LANCZOS', Image.ANTIALIAS)
                img.thumbnail(max_size, resample)

                buffer = io.BytesIO()
                img.save(buffer, format='JPEG', quality=85)
                buffer.seek(0)

                # monta novo nome com extensão .jpg
                try:
                    base_name = self.imagem.name.rsplit('.', 1)[0]
                except Exception:
                    base_name = 'perfil_{}'.format(self.usuario.pk)
                new_name = f"{base_name}.jpg"

                # salva no campo sem chamar save novamente
                self.imagem.save(new_name, ContentFile(buffer.read()), save=False)
        except Exception:
            # se algo falhar durante o processamento, não bloquear o save
            pass

        super().save(*args, **kwargs)

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
