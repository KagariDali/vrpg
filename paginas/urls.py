
from django.urls import path
from .views import Inicio, SobreView

urlpatterns = [
    path ("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]
