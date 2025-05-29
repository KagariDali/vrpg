
from django.urls import path
from .views import (Inicio, SobreView,  BotCreate, CategoriaCreate, AvaliacaoCreate, ComentarioCreate, 
BotUpdate, CategoriaUpdate, AvaliacaoUpdate, ComentarioUpdate,
BotDelete, CategoriaDelete, AvaliacaoDelete, ComentarioDelete)

urlpatterns = [

    path("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),


    path('cadastrar/bot/', BotCreate.as_view(), name="cadastrar-bot"),
    path('cadastrar/avaliar/', AvaliacaoCreate.as_view(), name="Avalie"),
    path('cadastrar/comentario/', ComentarioCreate.as_view(), name="Comente"),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),

    path('atualizar/bot/<int:pk>/', BotUpdate.as_view(), name="Atualizar-bot"),
    path('atualizar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name="Atualizar-Categoria"),
    path('atualizar/comentario/<int:pk>/', ComentarioUpdate.as_view(), name="Editar-Comentario"),
    path('atualizar/avaliacao/<int:pk>/', AvaliacaoUpdate.as_view(), name="Atualizar-Avaliacao"),

    path('deletar/bot/<int:pk>/', BotDelete.as_view(), name="Deletar-bot"),
    path('deletar/categoria/<int:pk>/', CategoriaDelete.as_view(), name="Deletar-categoria"),
    path('deletar/comentario/<int:pk>/', ComentarioDelete.as_view(), name="Deletar-comentario"),
    path('deletar/avaliacao/<int:pk>/', AvaliacaoDelete.as_view(), name="Deletar-avalaiacao"),
    

]

