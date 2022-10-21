from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("agregartarea/",views.agregartarea, name="agregartarea"),
        path("agregaractividad/",views.agregaractividad, name="agregaractividad"),
        path("eliminar/<int:tarea_id>/", views.eliminartarea, name= "eliminartarea"),
        path("editar/<int:tarea_id>/", views.editartarea, name="editartarea"),
        path("eliminar/<int:actividad_id>/", views.eliminaractividad, name= "eliminaractividad"),
        path("editar/<int:actividad_id>/", views.editaractividad, name="editaractividad"),
]
