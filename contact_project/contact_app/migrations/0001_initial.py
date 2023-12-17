# Generated by Django 5.0 on 2023-12-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('whatsapp', models.IntegerField(blank=True, max_length=100)),
                ('instagram', models.URLField(blank=True, max_length=100)),
                ('twitter', models.URLField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]