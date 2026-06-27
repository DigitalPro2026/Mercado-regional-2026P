from django.db import models
from django.contrib.auth.models import User

class Anuncio(models.Model):
    # Definimos tus 6 distritos específicos
    DISTRITOS = [
        ('campo_verde', 'Campo Verde'),
        ('pucallpa', 'Pucallpa'),
        ('honoria', 'Honoria'),
        ('tournavista', 'Tournavista'),
        ('nueva_requena', 'Nueva Requena'),
        ('neshuya', 'Neshuya'),
    ]
    
    # Definimos las categorías del mercado
    CATEGORIAS = [
        ('casas', 'Lotes, Casas y Terreno'),
        ('artefactos', 'Artefactos Eléctricos'),
        ('vehiculos', 'Vehículos'),
        ('otros', 'Otros productos'),
    ]

    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, verbose_name="Título del anuncio")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio (S/.)")
    distrito = models.CharField(max_length=20, choices=DISTRITOS, default='pucallpa')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='otros')
    imagen = models.ImageField(upload_to='fotos_anuncios/', null=True, blank=True, verbose_name="Foto del producto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    
class BannerPublicitario(models.Model):
    cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente/Negocio")
    imagen = models.ImageField(upload_to='banners/', verbose_name="Banner Horizontal (Recomendado 1200x300)")
    enlace_whatsapp = models.URLField(blank=True, null=True, verbose_name="Enlace de WhatsApp o Web (Opcional)")
    activo = models.BooleanField(default=True, verbose_name="¿Mostrar en la página?")
    fecha_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Publicidad de {self.cliente}"

    