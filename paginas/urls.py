
from django.urls import path
from .views import (Inicio, SobreView,  BotCreate, CategoriaCreate, AvaliacaoCreate, ComentarioCreate, 
BotUpdate, CategoriaUpdate, AvaliacaoUpdate, ComentarioUpdate,
BotDelete, CategoriaDelete, AvaliacaoDelete, ComentarioDelete)
urlpatterns = [

    path("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),


    path('Cadastrar/bot/', BotCreate.as_view(), name="cadastrar-bot"),
    path('Cadastrar/avaliar/', AvaliacaoCreate.as_view(), name="Avalie"),
    path('Cadastrar/Comentario/', ComentarioCreate.as_view(), name="Comente"),
    path('Cadastrar/Categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),

    path('Atualizar/bot/', BotUpdate.as_view(), name="Atualizar-bot"),
    path('Atualizar/Categoria/', CategoriaUpdate.as_view(), name="Atualizar-Categoria"),
    path('Atualizar/Comentario/', ComentarioUpdate.as_view(), name="Editar-Comentario"),
    path('Atualizar/Update/', AvaliacaoUpdate.as_view(), name="Atualizar-Avaliacao"),

    path('Deletar/bot/', BotDelete.as_view(), name="Deletar-bot"),
    path('Deletar/categoria/', CategoriaDelete.as_view(), name="Deletar-categoria"),
    path('Deletar/Comentario/', ComentarioDelete.as_view(), name="Deletar-comentario"),
    path('Deletar/Avaliacao/', AvaliacaoDelete.as_view(), name="Deletar-avalaiacao"),
    

]

