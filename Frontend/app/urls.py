from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('subirConfiguracion', views.subirConfig, name='subirConfig'),
    path('subirConsumos', views.subirConsumos, name='subirConsumos'),
    path('panelOpciones', views.panelOpciones, name='panelOpciones'),
]