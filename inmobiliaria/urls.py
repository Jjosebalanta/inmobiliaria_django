from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('propiedad/<int:pid>/', views.detalle, name='detalle'),
    path('agendar/', views.agendar, name='agendar'),
    path('terminos/', views.terminos, name='terminos'),
]
 