# Generated by Django 3.1.3 on 2020-11-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201117_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='acount',
            name='acount',
            field=models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10),
        ),
    ]