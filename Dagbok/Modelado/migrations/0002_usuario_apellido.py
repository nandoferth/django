# Generated by Django 3.0.7 on 2020-06-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=30, null=True),
        ),
    ]