# Generated by Django 3.0.4 on 2020-03-15 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='korisnici',
        ),
    ]
