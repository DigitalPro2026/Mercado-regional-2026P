from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_bannerpublicitario_alter_anuncio_categoria_and_more'), # Revisa si tu último archivo en esa carpeta se llama así o similar
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='aprobado',
            field=models.BooleanField(default=False, verbose_name='¿Anuncio Aprobado para mostrarse?'),
        ),
    ]
