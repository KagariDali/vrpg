from django import template
from django.templatetags.static import static
from django.conf import settings
import os

register = template.Library()

@register.simple_tag
def profile_image(user):
    """Retorna a URL da imagem de perfil do usuário ou o fallback estático."""
    try:
        if not user or not user.is_authenticated:
            return static('img/no-photo.jpg')
        perfil = getattr(user, 'perfil', None)
        if perfil and getattr(perfil, 'imagem'):
            # imagem pode ser um FieldFile; verificar se possui url
            try:
                url = perfil.imagem.url
                if url:
                    return url
            except Exception:
                pass
    except Exception:
        pass
    return static('img/no-photo.jpg')


@register.simple_tag
def bot_image(bot):
    """Retorna URL da imagem do bot ou fallback para no-bot-photo.png (ou no-photo.jpg se não existir)."""
    try:
        if bot and getattr(bot, 'imagem'):
            try:
                url = bot.imagem.url
                if url:
                    return url
            except Exception:
                pass
    except Exception:
        pass

    # preferência por no-bot-photo.png, mas cai para no-photo.jpg se não existir
    candidate = os.path.join(settings.BASE_DIR, 'static', 'img', 'no-bot-photo.png')
    if os.path.exists(candidate):
        return static('img/no-bot-photo.png')
    return static('img/no-photo.jpg')


@register.filter(name='has_attr')
def has_attr(obj, attr_name):
    """Retorna True se o objeto tiver o atributo (não lança exceção)."""
    try:
        return hasattr(obj, attr_name)
    except Exception:
        return False
