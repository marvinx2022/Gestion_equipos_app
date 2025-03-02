from django import forms
from equipos.models import Indicador
from django.core.validators import RegexValidator



class ExcelUploadForm(forms.Form):
    
    file = forms.FileField()
    
    revision = forms.CharField(
        max_length=7,
        label='Revisión',
        validators=[
            RegexValidator(
                regex=r'(\d{2})/(\d{4})',  # Debe respetar formato ##/####, por ejemplo----> 39/2009
                message='Debe respetar formato ##/####, por ejemplo----> 39/2009',
                code='invalid_format'
            )
        ]
    )
    
    fecha_inicio = forms.DateField(
        label='Fecha Inicio',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    fecha_fin = forms.DateField(
        label='Fecha Fin',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    texto_revision = forms.CharField(
        max_length=50,
        label='Comentarios revisión',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )



"""
class ExcelUploadForm(forms.Form):
    
    file = forms.FileField()
    revision = forms.CharField(max_length=7, label='Revisión',
                                      validators=[
                                                    RegexValidator(
                                                        regex=r'(\d{2})/(\d{4})',  # Debe respetar formato ##/####, por ejemplo----> 01/2025
                                                        message='Debe respetar formato ##/####, por ejemplo----> 01/2025',
                                                        code='invalid_format'
                                                    )
                                                ]
                                      )
    fecha_inicio = forms.DateField(label='Fecha Inicio', widget=forms.SelectDateWidget)
    fecha_fin = forms.DateField(label='Fecha Fin', widget=forms.SelectDateWidget)
    texto_revision = forms.CharField(max_length=50, label='Comentarios revisión')
    
"""

class EstatusOpForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['estatus_operaciones']
        
        
class EstatusMaForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['estatus_mantenimiento']