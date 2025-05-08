
from django.urls import path
from .views import Inicio, SobreView
from .views import CampusCreate, CursoCreate

urlpatterns = [
    path ("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),

    path("adicionar/campus", CampusCreate.as_view(), name="inserur-campus"),
    path("adicionar/curso/", CursoCreate.as_view(), name="inserir-curso")
]
