from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Cliente, Produto, Fornecedor, Venda, Entrada, Estoque
from core.forms import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin, CreateUpdateAjaxMixin

def do_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

@login_required
def do_logout(request):
    logout(request)
    return redirect('login')


class HomeView(TemplateView):

    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'clientes': Cliente.objects.all().count(),
            'produtos': Produto.objects.all().count(),
            'fornecedores': Fornecedor.objects.all().count(),
            'tela': 'DASHBOARD'
        }

        return render(request,'core/home.html',context)

class LoginView(TemplateView):

    template_name = 'login.html'

class RegisterView(TemplateView):

    template_name = 'register.html'


class ClienteListView(ListView):

    template_name = 'core/clientes.html'
    model = Cliente
    paginate_by = 100

    def post(self,request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        context = {
            'object_list': Cliente.objects.all().order_by('nome'),
            'form': form
        }
        return render(request,'core/clientes.html', context)

    def get(self, request):
        form = ClienteForm()
        context = {
            'object_list': Cliente.objects.all().order_by('nome'),
            'form': form,
            'tela': 'CLIENTES'
        }
        return render(request, 'core/clientes.html', context)


class ClienteCreate(CreateView, SuccessMessageMixin):

    model = Cliente
    template_name_suffix = '_create_form'
    success_message = 'Cliente cadastrado com sucesso!'
    success_url = reverse_lazy('clientes')
    form_class = ClienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'Novo Cliente'
        return context


class ClienteEdit(UpdateView, SuccessMessageMixin):

    model = Cliente
    template_name_suffix = '_update_form'
    success_message = 'Cliente alterado com sucesso!'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'EDIÇÃO DE CLIENTE'
        return context


class ClienteDelete(DeleteAjaxMixin, SuccessMessageMixin, DeleteView):

    model = Cliente
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente excluido com sucesso!'

class ProdutoList(ListView):

    model = Produto
    template_name = 'core/produtos.html'
    paginate_by = 100

    def get_queryset(self):
        return Produto.objects.all().order_by('nome_produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'PRODUTOS'
        return context


class ProdutoNovo(CreateView, PassRequestMixin,SuccessMessageMixin):

    model = Produto
    template_name = 'core/produto_novo.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto cadastrado com sucesso'
    form_class = ProdutoForm


class ProdutoEdit(UpdateView, PassRequestMixin, SuccessMessageMixin):

    model = Produto
    template_name = 'core/produto_update_form.html'
    form_class = ProdutoForm
    success_message = 'Produto alterado com sucesso!'
    success_url = reverse_lazy('produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'EDIÇÃO DE PRODUTO'
        return context

class ProdutoDelete(DeleteAjaxMixin, SuccessMessageMixin, DeleteView):

    model = Produto
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto excluido com sucesso!'


class VendaList(ListView):

    model = Venda
    paginate_by = 100
    template_name = 'core/vendas.html'

    def get_queryset(self):
        return Venda.objects.all().order_by('data_venda')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'VENDAS'
        return context



class VendaCreate(CreateView, SuccessMessageMixin):

    model = Venda
    form_class = VendaForm
    template_name = 'core/venda_create_form.html'
    success_message = 'Entrada cadastrada com sucesso'
