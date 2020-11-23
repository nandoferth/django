# Generated by Django 3.1.3 on 2020-11-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='acount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30, null=True)),
                ('price', models.FloatField(max_length=30, null=True)),
                ('sizesProduct', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=3)),
                ('storeStock', models.CharField(choices=[('Out', 'not available'), ('In', 'availabel')], max_length=3)),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='firstName',
        ),
    ]