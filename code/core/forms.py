from django import forms
from core.models import *
from bootstrap_modal_forms.mixins import PopRequestMixin


class ClienteForm(forms.ModelForm):

    estado = forms.ChoiceField(label='Estado',choices=UF_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

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
        }

class ProdutoForm(PopRequestMixin,forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'nome_produto': forms.TextInput(attrs={'class':'form-control'}),
            'peso': forms.NumberInput(attrs={'class':'form-control'}),
            'data_validade': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EstoqueForm(PopRequestMixin, forms.ModelForm):

    class Meta:
        model = Estoque
        fields = '__all__'

        widgets = {
            'data_entrada': forms.TextInput(attrs={'class':'form-control','type':'date'}),
        }


class FornecedorForm(forms.ModelForm):

    estado = forms.ChoiceField(label='Estado', choices=UF_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Fornecedor
        fields = '__all__'

        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'id': 'cnpj', 'placeholder': '__.___.___/____-__'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'id': 'telefone', 'placeholder': '( __ ) _  ____-____'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
        }