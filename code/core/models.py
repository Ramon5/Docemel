from django.db import models

class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=130, blank=True, null=True)
    data_nasc = models.DateField('Data de Nascimento', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=16)
    email = models.EmailField('E-mail', null=True, blank=True)
    rua = models.CharField('Rua', max_length=120, blank=True, null=True)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=80, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=40, blank=True, null=True)
    estado = models.CharField('Estado', max_length=130, blank=True, null=True)
    telefone = models.CharField('Contato', max_length=20, blank=True, null=True)

    @property
    def get_nome(self):
        return self.nome
    
    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    razao_social = models.CharField('Razão Social', max_length=90)
    nome_fantasia = models.CharField('Razão Social', max_length=90)
    cnpj = models.CharField('CNPJ',max_length=16)
    rua = models.CharField('Rua', max_length=120, blank=True, null=True)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=80, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=40, blank=True, null=True)
    estado = models.CharField('Estado', max_length=130, blank=True, null=True)
    telefone = models.CharField('Contato', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    @property
    def get_nome(self):
        return self.nome_fantasia

    def __str__(self):
        return self.nome_fantasia


class Produto(models.Model):

    nome_produto = models.CharField('Produto', max_length=90, null=True, blank=True)
    peso = models.IntegerField('Peso')

    @property
    def get_produto(self):
        return self.nome_produto

    def __str__(self):
        return self.nome_produto



class Entrada(models.Model):

    data_entrada = models.DateField('Data')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    valor_custo = models.DecimalField('Custo', decimal_places=2, max_digits=15)
    quantidade = models.IntegerField('Quantidade')

    @property
    def get_data(self):
        return self.data_entrada

    def __str__(self):
        return self.data_entrada


class Venda(models.Model):

    data_venda = models.DateField('Data da Venda')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    valor = models.DecimalField('Valor Total', decimal_places=2, max_digits=15)

    @property
    def get_data(self):
        return self.data_venda

    def __str__(self):
        return self.data_venda


class Estoque(models.Model):

    produtos = models.ManyToManyField(Entrada)
    quantidade = models.IntegerField('Quantidade Total')

    def __str__(self):
        return self.quantidade
