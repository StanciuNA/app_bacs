# Generated by Django 4.0.4 on 2023-07-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livraison',
            name='livraison',
            field=models.ManyToManyField(through='bacsApp.Cargaison', to='bacsApp.bac'),
        ),
        migrations.AlterField(
            model_name='site',
            name='bac',
            field=models.ManyToManyField(through='bacsApp.Stock', to='bacsApp.bac'),
        ),
    ]
