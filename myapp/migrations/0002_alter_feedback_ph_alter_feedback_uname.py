# Generated by Django 4.2 on 2023-04-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='ph',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='uname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
