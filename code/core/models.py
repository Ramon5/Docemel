from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils import timezone
import re
from django.core.mail import send_mail

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)

SEXO = (
    (1,'MASCULINO'),
    (2,'FEMININO'),
)

class UsuarioManager(BaseUserManager):
    def create_user(self, username, first_name, last_name,email, password=None):
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name,email, password):

        user = self.create_user(
            username,
            first_name,
            last_name,
            email,
          
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(_('Username'), max_length=15, unique=True, help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    first_name = models.CharField(_('First Name'), max_length=30)
    last_name = models.CharField(_('Last Name'), max_length=30)
    email = models.EmailField(_('Email Address'), max_length=255, unique=True)
    sexo = models.IntegerField(_('Genre'),null=True,choices=SEXO)
    foto = models.ImageField(_('Photo'),null=True,upload_to='media')

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('Último login'), blank=True, null=True)
    is_admin = models.BooleanField(_('Administrator'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UsuarioManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    @property
    def is_superuser(self):
        return self.is_admin

    def get_full_name(self):
        full_name =   '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return self.first_name


class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=130, blank=True, null=True)
    data_nasc = models.DateField('Data de Nascimento', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=16)
    email = models.EmailField('E-mail', null=True, blank=True)
    rua = models.CharField('Rua', max_length=120, blank=True, null=True)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=80, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=40, blank=True, null=True)
    estado = models.CharField('Estado', max_length=2, blank=True, null=True, choices=UF_CHOICES)
    telefone = models.CharField('Contato', max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['nome']

    @property
    def get_nome(self):
        return self.nome
    
    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    razao_social = models.CharField('Razão Social', max_length=90)
    nome_fantasia = models.CharField('Razão Social', max_length=90)
    cnpj = models.CharField('CNPJ',max_length=18)
    rua = models.CharField('Rua', max_length=120, blank=True, null=True)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=80, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=40, blank=True, null=True)
    estado = models.CharField('Estado', max_length=2, blank=True, null=True, choices=UF_CHOICES)
    telefone = models.CharField('Contato', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    class Meta:
        ordering = ['razao_social']

    @property
    def nome(self):
        return self.nome_fantasia

    def __str__(self):
        return self.nome_fantasia


class Produto(models.Model):

    nome_produto = models.CharField('Produto', max_length=90, null=True, blank=True)
    numero_lote = models.CharField('Número do lote',max_length=12,null=True,blank=True)
    codigo_de_barras = models.CharField('Código de Barras', max_length=12,null=True,blank=True)
    data_validade = models.DateField('Data de Validade', null=True,blank=True)
    peso = models.IntegerField('Peso')

    class Meta:
        ordering = ['nome_produto']


    @property
    def produto(self):
        return self.nome_produto

    def __str__(self):
        return self.nome_produto


class Estoque(models.Model):

    data_entrada = models.DateField('Data')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    valor_custo = models.DecimalField('Custo', decimal_places=2, max_digits=15)
    quantidade = models.IntegerField('Quantidade')
    quantidade_minima = models.IntegerField('Quantidade Mínima')

    class Meta:
        ordering = ['data_entrada']

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

    class Meta:
        ordering = ['data_venda']

    @property
    def get_data(self):
        return self.data_venda

    def __str__(self):
        return self.data_venda

