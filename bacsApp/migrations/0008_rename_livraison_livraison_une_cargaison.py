# Generated by Django 4.0.4 on 2023-08-27 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bacsApp', '0007_utilisateur_mdp_utilisateur_nom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livraison',
            old_name='livraison',
            new_name='une_cargaison',
        ),
    ]
