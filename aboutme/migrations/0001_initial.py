# Generated by Django 5.0.1 on 2024-01-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=15)),
                ('line2', models.CharField(max_length=40)),
                ('line3', models.CharField(max_length=20)),
                ('btn', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feild', models.CharField(max_length=60)),
            ],
        ),
    ]
