# Generated by Django 4.0.5 on 2022-07-04 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_alter_familia_fechadenacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='familia',
            name='fechaDeNacimiento',
            field=models.DateField(default='2222-12-22'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='fechaDeNacimiento2',
            field=models.DateField(default='2222-12-22'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='fechaDeNacimiento3',
            field=models.DateField(default='2222-12-22'),
        ),
    ]
