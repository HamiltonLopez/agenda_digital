# Generated by Django 4.2.7 on 2023-11-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_address_contact_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]