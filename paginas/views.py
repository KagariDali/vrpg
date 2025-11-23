from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categoria, Bot, Avaliacao,Comentario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
# Adicione no início do arquivo depois das outras importações
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.shortcuts import get_object_or_404
from .forms import PerfilForm, BotForm
from .models import Perfil
from django.contrib import messages
from django.views.generic import TemplateView
from django.db.models import Q


# Mixin genérico para adicionar pesquisa via GET (parâmetro 'nome')
class SearchMixin:
    """Adiciona busca por uma string (GET param 'nome') sobre os campos
    listados em `search_fields` (lista de lookups Django, ex: 'nome',
    'bot__nome'). Se `search_fields` estiver vazio, não faz nada.
    """
    search_fields = []

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('nome', '').strip()
        if q and self.search_fields:
            query = Q()
            for f in self.search_fields:
                query |= Q(**{f + '__icontains': q})
            qs = qs.filter(query).distinct()
        return qs



class CadastroUsuarioView(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários', 'botao': 'Registrar-se'}


    def form_valid(self, form):

        url = super().form_valid(form)

        return url



# Users

'''class Inicio(TemplateView):
    template_name = 'paginas/index.html'''

# O chat GPT gerou este código para que eu possa rodar meu index. Perguntar ao professor o que isso faz.
class Inicio(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Bot.objects.select_related('categoria').all().order_by('-cadastro_em')
        # busca via GET param 'nome' (compatível com SearchMixin)
        q = self.request.GET.get('nome', '').strip()
        if q:
            query = Q()
            for f in ['nome', 'descricao', 'categoria__nome', 'link', 'usuario__username']:
                query |= Q(**{f + '__icontains': q})
            qs = qs.filter(query).distinct()

        context['bots'] = qs
        context['avaliacoes'] = Avaliacao.objects.all()
        context['comentarios'] = Comentario.objects.all()
        return context

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class UsuarioCreate(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastrar Usuário', 'botao': 'Cadastrar'}

class CategoriaCreate(LoginRequiredMixin, CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Categoria # classe criada no models.
    fields = [ 'nome' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Categorias de bot', 'botao' : 'Cadastrar'}


class BotCreate(LoginRequiredMixin, CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Bot # classe criada no models.
    form_class = BotForm
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Criar Bot', 'botao' : 'Cadastrar'}

    def form_valid(self, form):
        # pegar o usuário que está autenticado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    


class ComentarioCreate(LoginRequiredMixin, CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Comentario # classe criada no models.
    fields = [ 'comentario' , 'bot'] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Comente sobre o Bot', 'botao' : 'Cadastrar'}

    def form_valid(self, form):
        # pegar o usuário que está autenticado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Avaliacao # classe criada no models.
    fields = [ 'nota', 'bot' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'De uma nota ao Bot', 'botao' : 'Cadastrar'}

    def form_valid(self, form):
        # pegar o usuário que está autenticado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url                    

#######################################################################

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']  # você pode colocar mais campos se quiser
    template_name = 'paginas/formUpdate.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Atualizar Usuário', 'botao': 'Salvar alterações'}

    def get_object(self, queryset=None):
        # garante que o usuário só pode editar o próprio perfil
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Garante que exista um objeto Perfil para o usuário
        perfil = getattr(self.request.user, 'perfil', None)
        if perfil is None:
            perfil = Perfil.objects.create(usuario=self.request.user)
        context['perfil_form'] = PerfilForm(instance=perfil)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Garante que o perfil exista antes de processar o POST
        perfil = getattr(request.user, 'perfil', None)
        if perfil is None:
            perfil = Perfil.objects.create(usuario=request.user)

        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if perfil_form.is_valid():
            perfil_form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
        else:
            messages.error(request, 'Erro ao atualizar o perfil. Verifique os dados.')

        return super().post(request, *args, **kwargs)


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Categoria # classe criada no models.
    fields = [ 'nome' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Categorias de bot', 'botao' : 'Atualizar'}


class BotUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Bot # classe criada no models.
    form_class = BotForm
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Criar Bot', 'botao' : 'Atualizar'}

    def get_object(self, queryset =None):
        # Superuser pode editar qualquer bot; usuários normais apenas os próprios
        if self.request.user.is_superuser:
            return get_object_or_404(Bot, pk=self.kwargs['pk'])
        return get_object_or_404(Bot, pk=self.kwargs['pk'], usuario=self.request.user)


class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Comentario # classe criada no models.
    fields = [ 'comentario' , 'bot'] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Comente sobre o Bot', 'botao' : 'Atualizar'}
    def get_object(self, queryset =None):
        # Superuser pode editar qualquer comentário; usuários normais apenas os próprios
        if self.request.user.is_superuser:
            return get_object_or_404(Comentario, pk=self.kwargs['pk'])
        return get_object_or_404(Comentario, pk=self.kwargs['pk'], usuario=self.request.user)


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Avaliacao # classe criada no models.
    fields = [ 'nota', 'bot' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'De uma nota ao Bot', 'botao' : 'Atualizar'}
    def get_object(self, queryset =None):
        # Superuser pode editar qualquer avaliação; usuários normais apenas as próprias
        if self.request.user.is_superuser:
            return get_object_or_404(Avaliacao, pk=self.kwargs['pk'])
        return get_object_or_404(Avaliacao, pk=self.kwargs['pk'], usuario=self.request.user)


##############################################################################

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Usuário'}

    def get_object(self, queryset=None):
        # garante que o usuário só pode excluir o próprio perfil
        return self.request.user

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')


class BotDelete(LoginRequiredMixin, DeleteView):
    model = Bot
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset =None):
        # Superuser pode deletar qualquer bot; usuários normais apenas os próprios
        if self.request.user.is_superuser:
            return get_object_or_404(Bot, pk=self.kwargs['pk'])
        return get_object_or_404(Bot, pk=self.kwargs['pk'], usuario=self.request.user)


class ComentarioDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')
    def get_object(self, queryset =None):
        # Superuser pode deletar qualquer comentário; usuários normais apenas os próprios
        if self.request.user.is_superuser:
            return get_object_or_404(Comentario, pk=self.kwargs['pk'])
        return get_object_or_404(Comentario, pk=self.kwargs['pk'], usuario=self.request.user)


class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')
    def get_object(self, queryset =None):
        # Superuser pode deletar qualquer avaliação; usuários normais apenas as próprias
        if self.request.user.is_superuser:
            return get_object_or_404(Avaliacao, pk=self.kwargs['pk'])
        return get_object_or_404(Avaliacao, pk=self.kwargs['pk'], usuario=self.request.user)


##############################################################################


class BotListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Bot
    template_name = 'paginas/listas/bots.html'
    # campos que serão buscados quando o usuário enviar ?nome=...
    search_fields = ['nome', 'descricao', 'categoria__nome', 'link']


class UsuarioDetail(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # garante que o perfil exista
        perfil = getattr(user, 'perfil', None)
        if perfil is None:
            Perfil.objects.create(usuario=user)
        context['usuario'] = user
        context['bots'] = Bot.objects.filter(usuario=user).order_by('-cadastro_em')
        return context

class MeusBots(BotListView):
    def get_queryset(self):
        # reaproveita o comportamento do mixin (super() -> BotListView.get_queryset
        # que por sua vez chama ListView.get_queryset) e depois restringe ao usuário
        qs = super().get_queryset()
        return qs.filter(usuario=self.request.user)


class AvaliacaoListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Avaliacao
    template_name = 'paginas/listas/avaliacoes.html'
    search_fields = ['bot__nome', 'usuario__username']

class ComentarioListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Comentario
    template_name = 'paginas/listas/comentarios.html'
    search_fields = ['comentario', 'bot__nome', 'usuario__username']

class CategoriaListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Categoria
    template_name = 'paginas/listas/categorias.html'
    search_fields = ['nome']