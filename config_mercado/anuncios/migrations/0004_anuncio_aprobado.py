from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='aprobado',
            field=models.BooleanField(default=False, verbose_name='¿Anuncio Aprobado para mostrarse?'),
        ),
    ]
