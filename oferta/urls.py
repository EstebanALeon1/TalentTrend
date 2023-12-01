from django.urls import path
from . import views
urlpatterns = [
    path('index_empresa/', views.index_empresa, name='index_empresa'),
    path('login_empresa/',views.Ofertalist,name="login_empresa"),
    path('indexFormulario/',views.indexFormulario,name="index_formulario"),
    path('procesarFormulario/',views.procesarFormularioOferta,name="procesar_formulario"),
    path('editarusuario/<int:id_oferta>',views.editarOferta,name="editar_usuario"),
    path("actualizar_usuario/<int:id_oferta>",views.actualizarOferta, name="actualizar_usuario"),
    path("eliminar_usuario/<int:id_oferta>",views.eliminarOferta, name="eliminar_usuario"),
]
