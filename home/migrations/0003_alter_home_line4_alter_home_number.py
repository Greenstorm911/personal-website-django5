# Generated by Django 5.0.1 on 2024-01-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='line4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='home',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
