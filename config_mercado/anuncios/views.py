from django.shortcuts import render, redirect
from .models import Anuncio, BannerPublicitario
from .forms import AnuncioForm  # 👈 Importamos el formulario que acabas de crear

def pagina_inicio(request):
    distrito_filtrado = request.GET.get('distrito')
    if distrito_filtrado:
        anuncios = Anuncio.objects.filter(distrito=distrito_filtrado, aprobado=True).order_by('-fecha_creacion')
    else:
        anuncios = Anuncio.objects.filter(aprobado=True).order_by('-fecha_creacion')
        
    banners = BannerPublicitario.objects.filter(activo=True)
        
    return render(request, 'anuncios/inicio.html', {
        'anuncios': anuncios, 
        'distrito_seleccionado': distrito_filtrado,
        'banners': banners
    })

# 👇 ESTA ES LA NUEVA FUNCIÓN PARA SUBIR PRODUCTOS
def crear_anuncio(request):
    if request.method == 'POST':
        # request.POST trae los textos, request.FILES trae las fotos
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            # Por ahora, le asignamos el anuncio al administrador (tú) hasta que hagamos el login de usuarios
            anuncio.vendedor = request.user if request.user.is_authenticated else None
            # Si no estás logueado en la computadora, usaremos por defecto tu usuario ID 1
            if not anuncio.vendedor:
                from django.contrib.auth.models import User
                anuncio.vendedor = User.objects.first()
            anuncio.save()
            return redirect('inicio')  # Al terminar, lo regresa a la página principal
    else:
        form = AnuncioForm()
        
    return render(request, 'anuncios/crear_anuncio.html', {'form': form})
