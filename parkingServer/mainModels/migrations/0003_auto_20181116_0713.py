# Generated by Django 2.1.2 on 2018-11-16 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainModels', '0002_auto_20181116_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='row',
            old_name='activated',
            new_name='active',
        ),
    ]