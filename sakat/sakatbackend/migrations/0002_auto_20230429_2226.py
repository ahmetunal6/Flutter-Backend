# Generated by Django 3.2.9 on 2023-04-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sakatbackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tag',
            field=models.TextField(max_length=30, null=True),
        ),
    ]