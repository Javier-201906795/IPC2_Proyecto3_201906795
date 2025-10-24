from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('subirConfiguracion', views.subirConfig, name='subirConfig')
]