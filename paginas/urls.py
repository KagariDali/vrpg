
from django.urls import path
from .views import (Inicio, SobreView,  BotCreate, CategoriaCreate, AvaliacaoCreate, ComentarioCreate, 
BotUpdate, CategoriaUpdate, AvaliacaoUpdate, ComentarioUpdate,
BotDelete, CategoriaDelete, AvaliacaoDelete, ComentarioDelete)
from .views import BotListView, AvaliacaoListView, ComentarioListView, CategoriaListView, MeusBots
from django.contrib.auth import views as auth_views
from .views import CadastroUsuarioView
from django.urls import path
from .views import UsuarioUpdate
from .views import UsuarioDetail
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [

    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

    path("", Inicio.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),

    # logar, deslogar
    path("login/", auth_views.LoginView.as_view(template_name = 'paginas/form.html',
        extra_context = {'titulo': 'Autenticação', 
                         'botao' : 'Entrar'}), name="login"),

    path("senha/", auth_views.PasswordChangeView.as_view(template_name = 'paginas/form.html',
        extra_context = {'titulo': 'Atualizar senha', 
                         'botao' : 'Entrar'}), name="senha"),

        path(
        "alterar-senha/",
        PasswordChangeView.as_view(
            template_name="paginas/formUpdate.html",
            success_url=reverse_lazy("index"),
            extra_context={"titulo": "Alterar Senha", "botao": "Salvar nova senha"},
        ),
        name="alterar-senha",
    ),

    
    path("logout/", auth_views.LogoutView.as_view(next_page="index"), name="logout"),
    path("editar-usuario/", UsuarioUpdate.as_view(), name="editar-usuario"),
    path("perfil/", UsuarioDetail.as_view(), name="perfil"),


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

    path("listar/avaliacoes/", AvaliacaoListView.as_view(), name="listar-avaliacoes"),
    path("listar/comentarios/", ComentarioListView.as_view(), name="listar-comentarios"),
    path("listar/categorias/", CategoriaListView.as_view(), name="listar-categorias"),
    path("listar/bots/", BotListView.as_view(), name="listar-bots"),
    path("listar/meus-bots/", MeusBots.as_view(), name="listar-meus-bots"),

    # path("listar/meus-bots",)

]

