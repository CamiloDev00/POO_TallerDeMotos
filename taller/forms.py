from django import forms
from .models import Motocicleta

class MotocicletaForm(forms.ModelForm):
    class Meta:
        model = Motocicleta
        fields = ['patente', 'marca', 'modelo', 'cilindrada', 'dni_cliente']
        # Podemos agregar clases CSS para que se vea mejor después
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: AB123CD'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'dni_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
        }