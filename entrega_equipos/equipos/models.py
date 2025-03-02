from django.db import models
from datetime import timedelta
from django.forms import ValidationError
import re
from django.contrib.auth.models import AbstractUser, Permission, Group, User




#Validador para ingreso de semana/revisión en formato correcto 

def week_test(week):
        result = re.match(r'(\d{2})/(\d{4})', week)
        if result == None: 
            raise ValidationError("Ingresa el nombre de semana en formato correcto, ejemplo ===>  << 39/2009 >> ")



# Modelo para la carga de datos, desde excel  y datos con ingreso manual

class Indicador(models.Model):
 
    equipo = models.CharField(max_length=100)
    equipo_parado=models.CharField(max_length=5)
    texto = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, default="Especialidad")
    revision = models.CharField(max_length=7, validators=[week_test])
    texto_revision = models.CharField(max_length=100)
    dia= models.CharField(max_length=15)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estatus_operaciones=models.CharField(max_length=30, 
                                choices=[
                                    ('Programado', 'Programado'),
                                    ('Entregado', 'Entregado'),
                                    ('No entregado', 'No entregado')],
                                    default="Programado")
    estatus_mantenimiento=models.CharField(max_length=30, 
                                choices=[
                                    ('Programado', 'Programado'),
                                    ('Tomado', 'Tomado'),
                                    ('No tomado', 'No tomado')],
                                    default="Programado")
    def __str__(self):
        return f"{self.equipo} - {self.especialidad}"
    
    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"
    
    
# Modelo para la carga de datos  

class Revision(models.Model):
    
    nombre =  models.CharField(max_length=7, validators=[week_test])
    s_date = models.DateField()
    f_date = models.DateField()
    
    def __str__(self):
        
        return(f"Semana {self.nombre} --- del {self.s_date} al {self.f_date}")
    
    class Meta:
        verbose_name = "Semana"
        verbose_name_plural = "Semanas"




class Perfil(models.Model):
    
    PERFILES_CHOICES = [
        ('Operaciones', 'Operaciones'),
        ('Mantenimiento', 'Mantenimiento'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    perfil = models.CharField(max_length=20, choices=PERFILES_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.perfil}"
    
