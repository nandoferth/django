# Generated by Django 3.1.3 on 2020-11-20 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_acount_acount'),
    ]

    operations = [
        migrations.AddField(
            model_name='acount',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.customer'),
        ),
    ]
