from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('panelOpciones', views.panelOpciones, name='panelOpciones'),
    path('subirConfiguracion', views.subirConfig, name='subirConfig'),
    path('subirConsumos', views.subirConsumos, name='subirConsumos'),
    path('operacionesSistema', views.operacionesSistema, name='operacionesSistema'),
    path('consultaPanel', views.consultaPanel, name='consultaPanel'),
    path('crearNuevoDato', views.crearNuevoDato, name= 'crearNuevoDat'),
    path('seleccionarClientefacturacion', views.selcliFacturacion, name= 'selcliFacturacion'),
    path('facturacion', views.facturacion, name= 'facturacion'),
    path('ayuda', views.ayuda, name= 'ayuda'),
]