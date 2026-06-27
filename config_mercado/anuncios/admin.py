from django.contrib import admin
from .models import Anuncio, BannerPublicitario # 👈 Agregamos BannerPublicitario aquí

admin.site.register(Anuncio)
admin.site.register(BannerPublicitario) # 👈 Y esta nueva línea