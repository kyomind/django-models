# Generated by Django 3.2.13 on 2022-06-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cover',
            old_name='url',
            new_name='name',
        ),
    ]
