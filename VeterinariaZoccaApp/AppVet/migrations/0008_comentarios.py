# Generated by Django 4.0.3 on 2022-05-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVet', '0007_remove_animales_cliente_remove_animales_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido')),
                ('comentarios', models.CharField(max_length=20, verbose_name='comentario')),
            ],
        ),
    ]
