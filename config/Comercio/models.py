from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return '{}'.format(self.nombre)

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.nombre)

class Comuna(models.Model):
    nombre = models.CharField(max_length = 20)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model): 
    numero = models.CharField(max_length = 5)
    calle = models.CharField(max_length = 20) 
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str("{}, {}".format(self.calle,self.numero))

class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField()
    descuento = models.BooleanField()
    monto_final = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    
    def isDescuento(self):
        return self.descuento
    
    isDescuento.boolean = True
    isDescuento.short_description = 'Descuento'

    def __str__(self):
        return str('Venta al Cliente: {}'.format(self.cliente.nombre))

    

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    web = models.CharField(max_length=69)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE,null=True)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Detalle(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    cantidad = models.SmallIntegerField()
    venta = models.ForeignKey('Venta',on_delete=models.CASCADE,null=False)
    def __str__(self):
        return str("({}) {} a {}".format(self.cantidad,self.producto.nombre,self.venta.cliente.nombre))
