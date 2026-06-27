from django.contrib import admin
from .models import Anuncio, BannerPublicitario

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    # Esto creará columnas organizadas en tu panel
    list_display = ('titulo', 'distrito', 'categoria', 'precio', 'aprobado', 'fecha_creacion')
    # Esto te permitirá aprobar o desaprobar directamente desde la lista sin entrar a cada anuncio
    list_editable = ('aprobado',)
    # Agrega filtros laterales rápidos
    list_filter = ('aprobado', 'distrito', 'categoria')

admin.site.register(BannerPublicitario)
