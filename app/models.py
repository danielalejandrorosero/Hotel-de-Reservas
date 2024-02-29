from django.db import models

from django.contrib.auth.models import User




class Habitacion(models.Model):
    SIMPLE='simple'
    DOBLE='doble'
    MATRIMONIAL='matrimonial'
    
    TIPO_CHOICES = (
        (SIMPLE,'Simple'),
        (DOBLE,'Doble'),
        (MATRIMONIAL,'Matrimonial')
    )


    numero = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50,choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return str(self.numero)
    


class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    cedula = models.CharField(max_length=20)
    nro_pasaporte = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)


    def __str__(self):
        return self.cedula
    

class Reserva(models.Model):
    EFECTIVO='efectivo'
    TARJETA='tarjeta'
    TRANSFERENCIA='transferencia'


    FORMA_PAGO_CHOICES = (
        (EFECTIVO,'Efectivo'),
        (TARJETA,'Tarjeta'),
        (TRANSFERENCIA,'Transferencia')
    )


    PENDIENTE = 'pendiente'
    PAGADO = 'pagado'
    ELIMINADO = 'eliminado'
    
    ESTADO_CHOICES = (
        (PENDIENTE,'Pendiente'),
        (PAGADO,'Pagado'),
        (ELIMINADO,'Eliminado')
    )




    habitacion = models.ForeignKey(Habitacion,on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    montoPagado = models.DecimalField(max_digits=10,decimal_places=2)
    formaPago = models.CharField(max_length=100,choices=FORMA_PAGO_CHOICES)
    estado = models.CharField(max_length=100,choices=ESTADO_CHOICES)


    def __str__(self):
        return self.habitacion.numero