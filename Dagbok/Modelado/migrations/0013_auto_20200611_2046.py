# Generated by Django 3.0.7 on 2020-06-12 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modelado', '0012_auto_20200611_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='even_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='event_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='start_date',
            new_name='start',
        ),
    ]