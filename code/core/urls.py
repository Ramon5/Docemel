from django.urls import path
from core import views

urlpatterns = [
    path('home/', views.HomeView.as_view(),name='home'),
    path('',views.LoginView.as_view()),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/', views.RegisterView.as_view(), name='registro'),

    path('entrar/',views.do_login, name='do_login'),
    path('sair/',views.do_logout,name='sair'),

    # clientes
    path('clientes/',views.ClienteListView.as_view(),name='clientes'),
    path('novo_cliente/',views.ClienteCreate.as_view(),name='novo_cliente'),
    path('cliente_edit/<int:pk>/',views.ClienteEdit.as_view(),name='cliente_edit'),
    path('cliente_delete/<int:pk>/',views.ClienteDelete.as_view(),name='cliente_delete'),

    # produtos
    path('produtos/',views.ProdutoList.as_view(),name='produtos'),
    path('produto_create/',views.ProdutoNovo.as_view(),name='produto_create'),
    path('produto_edit/<int:pk>/',views.ProdutoEdit.as_view(),name='produto_edit'),
    path('produto_delete/<int:pk>/',views.ProdutoDelete.as_view(),name='produto_delete'),

    # estoque
    path('estoque/', views.EstoqueList.as_view(), name='estoque'),
    path('estoque_create/', views.EstoqueNovo.as_view(), name='entrada_create'),

    # fornecedores
    path('fornecedores/',views.FornecedorList.as_view(), name='fornecedores'),
    path('fornecedor_create/',views.FornecedorCreate.as_view(),name='fornecedor_create'),
    path('fornecedor_edit/<int:pk>/',views.FornecedorEdit.as_view(),name='fornecedor_edit'),
    path('fornecedor_delete/<int:pk>/',views.FornecedorDelete.as_view(),name='fornecedor_delete'),


]