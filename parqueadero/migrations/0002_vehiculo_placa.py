# Generated by Django 2.0.2 on 2018-04-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parqueadero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(default='No title', max_length=50),
        ),
    ]
