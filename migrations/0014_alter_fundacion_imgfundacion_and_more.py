# Generated by Django 4.0.4 on 2022-06-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_fundacion_alter_contacto_mailf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundacion',
            name='imgFundacion',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagenProd',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
    ]
