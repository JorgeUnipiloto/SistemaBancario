# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Transaccion)
admin.site.register(Registro)
admin.site.register(Seguridad)

