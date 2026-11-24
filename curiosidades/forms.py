from django import forms

from .models import Carro, Comentario, Curiosidade, Marca


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nome", "pais", "ano_fundacao", "descricao", "foto"]


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ["modelo", "ano", "descricao", "foto"]


class CuriosidadeForm(forms.ModelForm):
    class Meta:
        model = Curiosidade
        fields = ["titulo", "texto"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        widgets = {"texto": forms.Textarea(attrs={"rows": 3, "placeholder": "Escreva seu comentário..."})}
        labels = {"texto": ""}
