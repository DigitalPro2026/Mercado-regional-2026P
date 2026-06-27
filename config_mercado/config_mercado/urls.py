from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from anuncios.views import pagina_inicio, crear_anuncio # 👈 Importamos crear_anuncio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicio, name='inicio'),
    path('publicar/', crear_anuncio, name='crear_anuncio'), # 👈 Nueva dirección URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)