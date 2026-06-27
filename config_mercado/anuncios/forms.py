from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        # Le decimos a Django qué campos queremos que llene el usuario
        fields = ['titulo', 'descripcion', 'precio', 'distrito', 'categoria', 'imagen']
        
        # Le agregamos diseños de Bootstrap a cada campo para que se vea bien en celulares
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Vendo TV Samsung 50 pulgadas'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el estado del producto, contacto, etc.'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1200.00'}),
            'distrito': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }