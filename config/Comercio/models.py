from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return '{}'.format(self.nombre)

class Detalle(models.Model):
    cantidad = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.cantidad)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Venta(models.Model, Producto, Detalle):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField()
    descuento = models.FloatField()
    monto_final = models.FloatField()
    Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def MontoFinal(self, Producto.precio, Detalle.cantidad):
        precio = Producto.precio
        cantidad = Detalle.cantidad
        monto_final = precio * cantidad

    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=40)
    comuna = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.calle)


class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    web = models.CharField(max_length=69)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

