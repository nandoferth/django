# Generated by Django 3.0.7 on 2020-06-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelado', '0008_auto_20200610_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviarsolicitud',
            name='follwers',
            field=models.ManyToManyField(blank=True, related_name='is_followers', to='Modelado.Usuario'),
        ),
    ]