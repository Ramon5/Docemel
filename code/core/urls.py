from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', login_required(views.HomeView.as_view()),name='home'),
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


]