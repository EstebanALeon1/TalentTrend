from django.urls import path
from . import views
urlpatterns = [
    path('login_usuario/', views.login_usuario, name='login_empresa'),
    path('index/', views.index, name='index'),
    path('experiencia_list/',views.Experiencialist,name="experiencialist"),
    path('indexFormulario/',views.indexFormulario,name="index_formulario_experiencia"),
    path('procesarFormulario/',views.procesarFormularioExperiencia,name="procesar_formulario_experiencia"),
    path('editarexperiencia/<int:id_experiencia>',views.editarExperiencia,name="editar_experiencia"),
    path("actualizar_uexperiencia/<int:id_experiencia>",views.actualizarExperiencia, name="actualizar_experiencia"),
    path("eliminar_experiencia/<int:id_experiencia>",views.eliminarExperiencia, name="eliminar_experiencia"),
]
