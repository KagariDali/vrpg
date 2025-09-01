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
        context['bots'] = Bot.objects.select_related('categoria').all().order_by('-cadastro_em')
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
    fields = [ 'nome', 'descricao', 'categoria', 'link' ] # lista com os nomes dos atributos.
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
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Atualizar Usuário', 'botao': 'Salvar alterações'}

    def get_object(self, queryset=None):
        # garante que o usuário só pode editar o próprio perfil
        return self.request.user


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Categoria # classe criada no models.
    fields = [ 'nome' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Categorias de bot', 'botao' : 'Atualizar'}


class BotUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Bot # classe criada no models.
    fields = [ 'nome', 'descricao', 'categoria', 'link' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Criar Bot', 'botao' : 'Atualizar'}

    def get_object(self, queryset =None):
        obj = get_object_or_404(Bot, pk=self.kwargs['pk'], usuario=self.request.user)


class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Comentario # classe criada no models.
    fields = [ 'comentario' , 'bot'] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Comente sobre o Bot', 'botao' : 'Atualizar'}


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Avaliacao # classe criada no models.
    fields = [ 'nota', 'bot' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'De uma nota ao Bot', 'botao' : 'Atualizar'}


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
        obj = get_object_or_404(Bot, pk=self.kwargs['pk'], usuario=self.request.user)


class ComentarioDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')


class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'paginas/formExcluir.html'
    success_url = reverse_lazy('index')


##############################################################################


class BotListView(LoginRequiredMixin, ListView):
    model = Bot
    template_name = 'paginas/listas/bots.html'

    def get_queryset(self):
        
        if(self.request.user.is_superuser):
            return Bot.objects.all()
        else:
            return Bot.objects.filter(usuario=self.request.user)


class AvaliacaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'paginas/listas/avaliacoes.html'

class ComentarioListView(LoginRequiredMixin, ListView):
    model = Comentario
    template_name = 'paginas/listas/comentarios.html'

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'paginas/listas/categorias.html'