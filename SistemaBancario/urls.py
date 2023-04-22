"""
URL configuration for SistemaBancario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Modulos.Cuenta import views
from django.views.generic import TemplateView

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
    
    path('admin/', admin.site.urls, name='admin'),
    path('api/personas/', views.PersonaList.as_view(), name='persona_list'),
    path('api/personas/<int:pk>/', views.PersonaDetail.as_view(), name='persona_detail'),
    path('api/usuarios/', views.UsuarioList.as_view(), name='usuario_list'),
    path('api/usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario_detail'),
    path('api/cuentas/', views.CuentaList.as_view(), name='cuenta_list'),
    path('api/cuentas/<int:pk>/', views.CuentaDetail.as_view(), name='cuenta_detail'),
    path('api/transacciones/', views.TransaccionList.as_view(), name='transaccion_list'),
    path('api/transacciones/<int:pk>/', views.TransaccionDetail.as_view(), name='transaccion_detail'),
    path('api/registros/', views.RegistroList.as_view(), name='registro_list'),
    path('api/registros/<int:pk>/', views.RegistroDetail.as_view(), name='registro_detail'),
    path('api/seguridad/', views.SeguridadList.as_view(), name='seguridad_list'),
    path('api/seguridad/<int:pk>/', views.SeguridadDetail.as_view(), name='seguridad_detail'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('consignacion/', views.consignar, name='consignar'),
    path('consultarr/', views.consultar, name='consultar'),
    #path('consignar/', views.consignacion, name='consignar'),

    

]

