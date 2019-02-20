from django import forms
from core.models import *
from bootstrap_modal_forms.mixins import PopRequestMixin


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'data_nasc': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control','id':'cpf','placeholder':'___.___.___-__'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email'}),
            'telefone': forms.TextInput(attrs={'class':'form-control','id':'telefone','placeholder':'( __ ) _  ____-____'}),
            'rua': forms.TextInput(attrs={'class':'form-control'}),
            'numero': forms.NumberInput(attrs={'class':'form-control'}),
            'bairro': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProdutoForm(PopRequestMixin,forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'nome_produto': forms.TextInput(attrs={'class':'form-control'}),
            'peso': forms.NumberInput(attrs={'class':'form-control'}),
        }


class VendaForm(PopRequestMixin, forms.ModelForm):

    class Meta:
        model = Venda
        fields = '__all__'