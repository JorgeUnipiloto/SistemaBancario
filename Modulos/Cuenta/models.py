from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        txt = "{0} {1} (Cedula: {2})"
        return txt.format(self.nombres, self.apellidos, self.cedula)


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        txt = "UserName: {0}"
        return txt.format(self.username)


class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        txt = "Cuenta N°: {0}"
        return txt.format(self.id)


class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "Transaccion desde la cuenta {1} {0} por el valor de {2}. Fecha: {3} "
        return txt.format(self.cuenta, self.tipo, self.valor, self.fecha)


class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Registro N°: {0} por el: {1}| Fecha: {2}"
        return txt.format(self.id, self.usuario, self.fecha)


class Seguridad(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=200)

    def __str__(self):
        txt = "Seguridad: {0}"
        return txt.format(self.usuario)




