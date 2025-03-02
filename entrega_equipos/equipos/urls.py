from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from equipos.views import index, carga_exitosa, carga_datos, mostrar_datos_cargados, equipo_parado, actualizar_estatus, actualizar_estatus_equipos, actualizar_estatus_operaciones, actualizar_estatus_mantenimiento

urlpatterns = [
    path('', index, name="Index"),
    path('carga_exitosa', carga_exitosa, name="CargaExitosa"),
    path('carga_datos', carga_datos, name="CargaDatos"),
    path('mostrar_datos', mostrar_datos_cargados, name="MostrarDatos"),
    path('equipos_parados', equipo_parado, name="EquipoParado"),
    path('actualizar_estatus/<int:id>/', actualizar_estatus, name='actualizar_estatus'),
    path('actualizar_estatus_equipos', actualizar_estatus_equipos, name='Actualizar'),
    path('actualizar_estatus_operaciones/<int:id>/', actualizar_estatus_operaciones, name='ActualizarEstatusOperaciones'),
    path('actualizar_estatus_mantenimiento/<int:id>/', actualizar_estatus_mantenimiento, name='ActualizarEstatusMantenimiento'),
    path('login/', LoginView.as_view(template_name='equipos/login.html'), name='Login'),
    path('logout/', LogoutView.as_view(next_page='Index'), name='Logout')
]

