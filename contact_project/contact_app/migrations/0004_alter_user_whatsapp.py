# Generated by Django 5.0 on 2023-12-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_rename_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='whatsapp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
