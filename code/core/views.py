from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.models import Cliente, Produto, Fornecedor, Venda,Estoque
from core.forms import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import DetailView,FormView,RedirectView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from extras.mixins import DangerMessageMixin,WarningMessageMixin,InfoMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin, CreateUpdateAjaxMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters



class HomeView(LoginRequiredMixin,TemplateView):

    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'clientes': Cliente.objects.all().count(),
            'produtos': Produto.objects.all().count(),
            'fornecedores': Fornecedor.objects.all().count(),
            'tela': 'DASHBOARD'
        }

        return render(request,'core/home.html',context)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url =  reverse_lazy("home")

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)



class LogoutView(LoginRequiredMixin,RedirectView):

    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(TemplateView):

    template_name = 'register.html'



## Cliente

class ClienteListView(LoginRequiredMixin,ListView):

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


class ClienteCreate(LoginRequiredMixin,CreateView, SuccessMessageMixin):

    model = Cliente
    template_name_suffix = '_create_form'
    success_message = 'Cliente cadastrado com sucesso!'
    success_url = reverse_lazy('clientes')
    form_class = ClienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'NOVO CLIENTE'
        return context


class ClienteEdit(LoginRequiredMixin,UpdateView, SuccessMessageMixin):

    model = Cliente
    template_name_suffix = '_update_form'
    success_message = 'Cliente alterado com sucesso!'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'EDIÇÃO DE CLIENTE'
        return context


class ClienteDelete(LoginRequiredMixin,DeleteAjaxMixin, DangerMessageMixin, DeleteView):

    model = Cliente
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('clientes')
    danger_message = 'Cliente excluido com sucesso!'


## Produtos

class ProdutoList(LoginRequiredMixin,ListView):

    model = Produto
    template_name = 'core/produtos.html'
    paginate_by = 100

    def get_queryset(self):
        return Produto.objects.all().order_by('nome_produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'PRODUTOS'
        return context


class ProdutoNovo(LoginRequiredMixin,CreateView, PassRequestMixin,SuccessMessageMixin):

    model = Produto
    template_name = 'core/produto_novo.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto cadastrado com sucesso'
    form_class = ProdutoForm


class ProdutoEdit(LoginRequiredMixin,UpdateView, PassRequestMixin, SuccessMessageMixin):

    model = Produto
    template_name = 'core/produto_update_form.html'
    form_class = ProdutoForm
    success_message = 'Produto alterado com sucesso!'
    success_url = reverse_lazy('produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'EDIÇÃO DE PRODUTO'
        return context

class ProdutoDelete(LoginRequiredMixin,DeleteAjaxMixin, DangerMessageMixin, DeleteView):

    model = Produto
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('produtos')
    danger_message = 'Produto excluido com sucesso!'


## Estoque
class EstoqueList(LoginRequiredMixin,ListView):

    model = Estoque
    template_name = 'core/estoque_list.html'
    paginate_by = 100

    def get_queryset(self):
        return Estoque.objects.select_related('produto').select_related('fornecedor').all().order_by('id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'ESTOQUE'
        return context


class EstoqueNovo(LoginRequiredMixin,CreateView, PassRequestMixin,SuccessMessageMixin):

    model = Produto
    template_name = 'core/entrada_estoque.html'
    success_url = reverse_lazy('estoque')
    success_message = 'Produto cadastrado com sucesso'
    form_class = EstoqueForm


## Fornecedor

class FornecedorList(LoginRequiredMixin,ListView):

    model = Fornecedor
    template_name = 'core/fornecedor_list.html'
    paginate_by = 100

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'FORNECEDORES'
        return context

class FornecedorCreate(LoginRequiredMixin,CreateView, SuccessMessageMixin):

    model = Fornecedor
    template_name_suffix = '_create_form'
    success_message = 'Fornecedor cadastrado com sucesso!'
    success_url = reverse_lazy('fornecedores')
    form_class = FornecedorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'NOVO FORNECEDOR'
        return context


class FornecedorEdit(LoginRequiredMixin,UpdateView, SuccessMessageMixin):

    model = Fornecedor
    template_name_suffix = '_update_form'
    success_message = 'Fornecedor alterado com sucesso!'
    form_class = FornecedorForm
    success_url = reverse_lazy('fornecedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'EDIÇÃO DE FORNECEDOR'
        return context


class FornecedorDelete(LoginRequiredMixin,DeleteAjaxMixin, DangerMessageMixin, DeleteView):

    model = Fornecedor
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('fornecedores')
    danger_message = 'Fornecedor excluido com sucesso!'

# Profile
class ProfileView(LoginRequiredMixin,TemplateView):

    template_name = 'profile.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tela'] = 'MEUS DADOS'
        return context