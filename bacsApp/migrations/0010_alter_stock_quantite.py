# Generated by Django 4.0.4 on 2023-09-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacsApp', '0009_rename_documnet_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantite',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
