# Generated by Django 4.2.3 on 2023-07-25 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barrioprivado', '0002_alter_staff_sector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='codigo_sector',
            new_name='codigo',
        ),
    ]