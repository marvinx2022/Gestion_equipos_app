# App de gestión de entrega de equipos para mantenimiento. 

Web App desarrollada para gestionar y registrar los trabajos de mantenimiento de equipos, así como el registro de ejecución de trabajos. 

## Problema planteado

Generar una Web App que permita generar el registro de los trabajo planificados para periodos semanales con las siguientes generalidades:

*   Permite creación de perfiles de usuario para áreas "Mantenimeinto" y "Operaciones", con diferentes funciones para cada sector. 
*   Permite cargar la información de los trabajos programados en un archivo Excel, para luego escribirlos en una base de datos. 
*   Se crean campos nuevos para reflejar si los equipos son entregados desde operaciones, y si son intervenidos por mantenimiento. 
*   Se registran todas las acciones en la base de datos. 
*   Permite realizar filtrado de datos. 
*   Se requiere un usuario Adminsitrador el cual puede generar nuevos usuarios con el perfil solicitado. 
*   Se requiere que se valide el nombre del periodo de tiempo en base al formado de número de semana estándar (Por ejemplo "39/2009" corresponde a la semana No. 39 del 2009, que incluye las fechas del 21 al 27 de septiembre de 2009)
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
- Se genera una interfaz responsiva para poder ser visualizada en diferentes dispositivos de manera adecuada.

## Algunas capturas de la Web App en ejecución

- Vista restringida sin Login de usuario:
![app1_sin login](https://github.com/user-attachments/assets/48c74559-afe4-42c4-af03-d506c4bf78d0)



- Acceso de usuario:
![app2_login](https://github.com/user-attachments/assets/cbffcdd0-8e65-412f-aa49-28ec21d98afa)



- Uso del Admin de Django para gestionar usuarios, creación, asignación de perfiles:
![app3_djangoadmin](https://github.com/user-attachments/assets/b1a25acd-0674-4e94-a9c6-85de471c7a74)



- Carga de  datos del programa semanal:
![app4_carga de datos](https://github.com/user-attachments/assets/273a7bfd-864b-4dbb-8492-35b536fce223)



- Pantalla de confirmación de carga de datos:
![APP5_DATOS CARGADS](https://github.com/user-attachments/assets/cf02f143-ed06-4686-84f7-66d81aff273b)



- Filtrado de datos para visualización:
![APP6_FILTRADO DE DATOS](https://github.com/user-attachments/assets/dd6c6c85-9867-4659-abd3-8b5a640050a3)



- Actualización de estatus, según perfil del usuario:
![app7_actualizar estatus](https://github.com/user-attachments/assets/80ae11fa-96db-444d-a196-f2811929f2d9)

