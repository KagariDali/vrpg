from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categoria, Bot, Avaliacao,Comentario
from django.urls import reverse_lazy

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


class CategoriaCreate(CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Categoria # classe criada no models.
    fields = [ 'nome' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Categorias de bot', 'botao' : 'Cadastrar'}


class BotCreate(CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Bot # classe criada no models.
    fields = [ 'nome', 'descricao', 'categoria', 'link' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Criar Bot', 'botao' : 'Cadastrar'}


class ComentarioCreate(CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Comentario # classe criada no models.
    fields = [ 'comentario' , 'bot'] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Comente sobre o Bot', 'botao' : 'Cadastrar'}


class AvaliacaoCreate(CreateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Avaliacao # classe criada no models.
    fields = [ 'nota', 'bot' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'De uma nota ao Bot', 'botao' : 'Cadastrar'}

#######################################################################

class CategoriaUpdate(UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Categoria # classe criada no models.
    fields = [ 'nome' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Categorias de bot', 'botao' : 'Cadastrar'}


class BotUpdate(UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Bot # classe criada no models.
    fields = [ 'nome', 'descricao', 'categoria', 'link' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Criar Bot', 'botao' : 'Cadastrar'}


class ComentarioUpdate(UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Comentario # classe criada no models.
    fields = [ 'comentario' , 'bot'] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'Comente sobre o Bot', 'botao' : 'Cadastrar'}


class AvaliacaoUpdate(UpdateView):
    template_name = "paginas/form.html" # arquivo html com o <form>.
    model = Avaliacao # classe criada no models.
    fields = [ 'nota', 'bot' ] # lista com os nomes dos atributos.
    success_url = reverse_lazy('index') # name da url para redirecionar.
    extra_context = {'titulo': 'De uma nota ao Bot', 'botao' : 'Cadastrar'}


##############################################################################

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'paginas\formExcluir.html'
    success_url = reverse_lazy('index')

class BotDelete(DeleteView):
    model = Bot
    template_name = 'paginas\formExcluir.html'
    success_url = reverse_lazy('index')

class ComentarioDelete(DeleteView):
    model = Comentario
    template_name = 'paginas\formExcluir.html'
    success_url = reverse_lazy('index')

class AvaliacaoDelete(DeleteView):
    model = Avaliacao
    template_name = 'paginas\formExcluir.html'
    success_url = reverse_lazy('index')
