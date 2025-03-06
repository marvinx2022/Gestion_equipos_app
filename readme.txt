# App de gestión de entrega de equipos a mantenimiento. 

Web App desarrollada para gestionar y registrar los trabajos de mantenimiento de equipos, así como el registro de ejecución de trabajos. 

## Problema planteado

Generar una Web App que permita generar el registro de los trabajo planificados para periodos semanales con las siguientes generalidades:

*   Permite creación de perfiles de usuario para áreas "Mantenimeinto" y "Operaciones", con diferentes funciones para cada sector. 
*   Permite cargar la información de los trabajos programados en un archivo Excel, para luego escribirlos en una base de datos. 
*   Se crean campos nuevos para reflejar si los equipos son entregados desde operaciones, y si son intervenidos por mantenimiento. 
*   Se registran todas las acciones en la base de datos. 
*   Permite realizar filtrado de datos. 
*   Se requiere un usuario Adminsitrador el cual puede generar nuevos usuarios con el perfil solicitado. 
*   Se requiere que se valide en nombre del periodo de tiempo en base al formado de número de semana estándar (Por ejemplo "39/2009" corresponde a la semana No. 39 del 2009, que incluye las fechas del 21 al 27 de septiembre de 2009)
*   Se debe tener una pestaña para cargar datos. 
*   Se debe tener una pestaña donde se muestren los datos para la fecha actual. 
*   Se debe tener una pestaña en la que se puedan gestionar los estatus de los trabajos para la fecha en curso, según el perfil del usuario que se encuentre logueado. 
*  El acceso sin login debe ser restringido a la información general de la App.


## General
- Desarrollada con Django, Bootstrapp, Base de datos SQLite
- Permite creación de perfiles de usuario para áreas "Manteniento" y "Operaciones", con diferentes funciones para cada sector. 
- Permite modificar y registrar las acciones sobre cada trabajo precargado. 
- La información de los trabajos para cada periodo se carga con un archivo Excel, se usa la librería Pandas para geestion de DataFrame. 
- Uso de Regex para validar información vs los formatos previamente establecidos. 

## Imágenes del proyecto


##
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## Requerimientos


## Instalación

Sigue estos pasos para instalar el proyecto:
1. Clona el repositorio
2. Instala las dependencias
3. Ejecuta el proyecto
