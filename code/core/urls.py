from django.urls import path
from core.views import *


urlpatterns = [
    # inicio
    path('home/', HomeView.as_view(),name='home'),
    path('',LoginView.as_view()),
    path('login/',LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(), name='registro'),
    path('sair/',LogoutView.as_view(),name='sair'),

    # profile
    path('profile/',ProfileView.as_view(),name='profile'),

    # clientes
    path('clientes/',ClienteListView.as_view(),name='clientes'),
    path('novo_cliente/',ClienteCreate.as_view(),name='novo_cliente'),
    path('cliente_edit/<int:pk>/',ClienteEdit.as_view(),name='cliente_edit'),
    path('cliente_delete/<int:pk>/',ClienteDelete.as_view(),name='cliente_delete'),

    # produtos
    path('produtos/',ProdutoList.as_view(),name='produtos'),
    path('produto_create/',ProdutoNovo.as_view(),name='produto_create'),
    path('produto_edit/<int:pk>/',ProdutoEdit.as_view(),name='produto_edit'),
    path('produto_delete/<int:pk>/',ProdutoDelete.as_view(),name='produto_delete'),

    # estoque
    path('estoque/', EstoqueList.as_view(), name='estoque'),
    path('estoque_create/', EstoqueNovo.as_view(), name='entrada_create'),

    # fornecedores
    path('fornecedores/',FornecedorList.as_view(), name='fornecedores'),
    path('fornecedor_create/',FornecedorCreate.as_view(),name='fornecedor_create'),
    path('fornecedor_edit/<int:pk>/',FornecedorEdit.as_view(),name='fornecedor_edit'),
    path('fornecedor_delete/<int:pk>/',FornecedorDelete.as_view(),name='fornecedor_delete'),


]