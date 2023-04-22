from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Persona, Usuario, Cuenta, Transaccion, Registro, Seguridad
from .serializers import PersonaSerializer, UsuarioSerializer, CuentaSerializer, TransaccionSerializer, RegistroSerializer, SeguridadSerializer



class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CuentaList(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class CuentaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class TransaccionList(generics.ListCreateAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer


class TransaccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer


class RegistroList(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer


class RegistroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer


class SeguridadList(generics.ListCreateAPIView):
    queryset = Seguridad.objects.all()
    serializer_class = SeguridadSerializer


class SeguridadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguridad.objects.all()
    serializer_class = SeguridadSerializer


def crear_cuenta(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre_id = request.POST.get('nombres')
        saldo = request.POST.get('saldo')

        # Buscamos la persona en la base de datos
        persona = Persona.objects.get(pk=nombre_id)

        # Creamos la cuenta con los datos ingresados
        cuenta = Cuenta(persona=persona, saldo=saldo)
        cuenta.save()

        # Mostramos un mensaje de éxito y redirigimos al usuario a otra página
        #messages.success(request, 'Su cuenta ha sido creada con éxito.')
        return redirect('crear_cuenta')
    
    # Si no se recibió un POST, renderizamos el formulario
    personas = Persona.objects.all()
    context = {'personas': personas}
    return render(request, 'base.html', context)

def consignar(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        cuenta_id = request.POST.get('cuentas')
        valor = request.POST.get('saldo1')
        tipo = request.POST.get('tipo')

        # Buscamos la persona en la base de datos
        cuenta = Cuenta.objects.get(pk=cuenta_id)

        # Creamos la cuenta con los datos ingresados
        transaccion = Transaccion(cuenta=cuenta, valor=valor, tipo=tipo)
        transaccion.save()

        # Mostramos un mensaje de éxito y redirigimos al usuario a otra página
        #messages.success(request, 'Su cuenta ha sido creada con éxito.')
        return redirect('consignar')
    
    # Si no se recibió un POST, renderizamos el formulario
    cuentas = Cuenta.objects.all()
    context = {'cuentas': cuentas}
    return render(request, 'base.html', context)

def consultar(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        cuenta_id = request.POST.get('cuentas1')
        
        # Buscamos la persona en la base de datos
        cuenta = Cuenta.objects.get(pk=cuenta_id)

        # Creamos la cuenta con los datos ingresados
        transaccion = Transaccion(cuenta=cuenta)
        transaccion.save()

        # Mostramos un mensaje de éxito y redirigimos al usuario a otra página
        #messages.success(request, 'Su cuenta ha sido creada con éxito.')
        return redirect('consultar')
    
    # Si no se recibió un POST, renderizamos el formulario
    cuentas = Cuenta.objects.all()
    context = {'cuentas': cuentas}
    return render(request, 'base.html', context)












