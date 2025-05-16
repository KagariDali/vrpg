
from django.urls import path
from .views import BotCreate, Inicio, SobreView
from .views import CampusCreate, CursoCreate

urlpatterns = [
    path ("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),

    path("adicionar/bot/", BotCreate.as_view(), name="inserir-bot"),
]
