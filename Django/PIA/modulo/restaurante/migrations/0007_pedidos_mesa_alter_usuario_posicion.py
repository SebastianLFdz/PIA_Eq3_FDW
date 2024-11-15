# Generated by Django 5.1.2 on 2024-11-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0006_alter_pedidos_idpedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='Mesa',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Posicion',
            field=models.CharField(choices=[('C', 'Chef'), ('M', 'Mesero'), ('A', 'Administrador')], max_length=1),
        ),
    ]
