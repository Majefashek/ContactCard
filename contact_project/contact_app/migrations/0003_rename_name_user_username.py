# Generated by Django 5.0 on 2023-12-09 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_alter_user_address_alter_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]