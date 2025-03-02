from django.shortcuts import render 
import pandas as pd
from django.shortcuts import render, redirect
from .models import Indicador, Revision
from .forms import ExcelUploadForm, EstatusOpForm, EstatusMaForm
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    
    if request.user.is_authenticated:
        
        perfil = request.user.perfil.perfil
        
    else:
    
        perfil = None
    
    perfil_usuario = perfil
    
    context = {
            
        'perfil_usuario' :perfil_usuario,
    }

    return render(request, "equipos/principal.html", context)
 
    

def carga_datos(request):
    
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["file"]
            revision = form.cleaned_data['revision']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            texto_revision=form.cleaned_data['texto_revision']
            df = pd.read_excel(excel_file)
            

            for _, row in df.iterrows():
                Indicador.objects.create(
                    dia=row['Texto 1'],
                    equipo=row['Equipo'] if pd.notna(row['Equipo']) else 'No cargado',
                    texto=row['Texto breve'],
                    especialidad=row['Clase actividad PM'],
                    equipo_parado=row['Est.instal.operación'], # Si el campo =0, indica que el equipo se requiere detenido, sobre estas filas se realizará la gestión.
                    revision=revision,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    texto_revision=texto_revision
                )
                
            Revision.objects.create(
                nombre =  revision,
                s_date = fecha_inicio,
                f_date =  fecha_fin 
            )


            return redirect("CargaExitosa") 
        
    else:
        
        form = ExcelUploadForm()





    if request.user.is_authenticated:
            
            perfil = request.user.perfil.perfil
            
    else:
        
            perfil = None
        
    perfil_usuario = perfil
        
    context = {
                
            'perfil_usuario' :perfil_usuario,
            "form": form,
                }




    return render(request, "equipos/carga_datos.html", context)



def carga_exitosa(request):
    return render(request, "equipos/carga_exitosa.html")


def mostrar_datos_cargados(request):
    # Obtener todos los datos de la base de datos
    data = Indicador.objects.all()

    # Filtrar los días, especialidades y revisiones distintas para el formulario
    dia = data.values('dia').distinct()
    especialidad = data.values('especialidad').distinct()
    revision = data.values('revision').distinct()

    # Recupera los parámetros de la URL
    dia_semana = request.GET.get('dia_semana', '')
    especialidad_param = request.GET.get('especialidad', '')
    revision_param = request.GET.get('revision', '')

    # Aplica los filtros si los parámetros existen
    if dia_semana:
        data = data.filter(dia=dia_semana)

    if especialidad_param:
        data = data.filter(especialidad=especialidad_param)

    if revision_param:
        data = data.filter(revision=revision_param)

    # Verifica si el usuario está autenticado y asigna el perfil
    if request.user.is_authenticated:
        perfil = request.user.perfil.perfil
    else:
        perfil = None
    
    perfil_usuario = perfil

    # Pasar el contexto para el template
    context = {
        'revision': revision,
        'dia': dia,
        'especialidad': especialidad,
        'perfil_usuario': perfil_usuario,
        'data': data,
    }

    return render(request, "equipos/datos.html", context)



def equipo_parado(request):
    
    weekdays={
            0:"LUNES",
            1:"MARTES",
            2:"MIERCOLES",
            3:"JUEVES",
            4:"VIERNES",
            5:"SABADO",
            6:"DOMINGO",
        }
    
    # Función para definir la revisión actual

    lista_semanas = Revision.objects.all()
    
    def es_semana_actual(lista):
    
        for semana in lista:
            
            if date.today()>=semana.s_date and date.today()<=semana.f_date:
                   
                semana_actual=semana.nombre
            
                print(f"La semana actual es: ====>  {semana_actual}, s_date-->{semana.s_date}, fecha {date.today()},  f_date-->{semana.f_date},")   
            
                return (semana_actual)

    
    semana_en_curso = es_semana_actual(lista_semanas)


    hoy = date.today().weekday()
    dia_actual=weekdays[hoy]
    
    equipos_parados = Indicador.objects.filter(equipo_parado=0).filter(dia=dia_actual).filter(revision=semana_en_curso)   # Es este caso si el campo equipo_parado=0 indica que el trabajo requiere entrega del equipo, es por lanaturaleza del sistekma de donde se obtiene la información de ingreso. 
    
    
    if request.user.is_authenticated:
        
        perfil = request.user.perfil.perfil
        
    else:
    
        perfil = None
    
    perfil_usuario = perfil
    
    context = {
        'equipos_parados': equipos_parados,
        'dia_actual': dia_actual,
        'semana_en_curso': semana_en_curso,
        'perfil_usuario': perfil_usuario,
    }   

    return render(request, 'equipos/equipos_detenidos.html', context)



def actualizar_estatus_equipos(request):
    
    weekdays={
            0:"LUNES",
            1:"MARTES",
            2:"MIERCOLES",
            3:"JUEVES",
            4:"VIERNES",
            5:"SABADO",
            6:"DOMINGO",
        }

    hoy = date.today().weekday()
    dia_actual=weekdays[hoy]
    
    
    
    lista_semanas = Revision.objects.all()
    
    def es_semana_actual(lista):
    
        for semana in lista:
            
            if date.today()>=semana.s_date and date.today()<=semana.f_date:
                   
                semana_actual=semana.nombre
            
                print(f"La semana actual es: ====>  {semana_actual}, s_date-->{semana.s_date}, fecha {date.today()},  f_date-->{semana.f_date},")   
            
                return (semana_actual)

    
    semana_en_curso = es_semana_actual(lista_semanas)
    
    equipos_parados = Indicador.objects.filter(equipo_parado=0).filter(dia=dia_actual).filter(revision=semana_en_curso)
    
    if request.user.is_authenticated:
        
        perfil = request.user.perfil.perfil
        
    else:
    
        perfil = None
    
    perfil_usuario = perfil
    


    context = {
        'equipos_parados': equipos_parados,
        'dia_actual': dia_actual,
        'semana_en_curso': semana_en_curso,       
        'perfil_usuario' :perfil_usuario
    }
    
    return render(request, 'equipos/actualizar_estatus.html', context)



def actualizar_estatus(request, id):
  
    if request.method == "POST": 
        nuevo_estatus = request.POST.get('estatus')  
        instancia = get_object_or_404(Indicador, id=id)  
        instancia.estatus = nuevo_estatus  
        instancia.save()  
        return JsonResponse({"mensaje": "Estatus actualizado correctamente"})  
    return JsonResponse({"mensaje": "Método no permitido"}, status=405)  



def actualizar_estatus_operaciones(request, id):
   
    instancia = get_object_or_404(Indicador, pk=id)

    if request.method == 'POST':
        form = EstatusOpForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()  
            return redirect('Actualizar') 
    else:
        form = EstatusOpForm(instance=instancia)

    return render(request, 'equipos/actualizar_estatus_operaciones.html', {'form': form, 'instancia': instancia})



def actualizar_estatus_mantenimiento(request, id):
   
    instancia = get_object_or_404(Indicador, pk=id)

    if request.method == 'POST':
        form = EstatusMaForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()  
            return redirect('Actualizar') 
    else:
        form = EstatusMaForm(instance=instancia)

    return render(request, 'equipos/actualizar_estatus_mantenimiento.html', {'form': form, 'instancia': instancia})