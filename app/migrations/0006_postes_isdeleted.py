# Generated by Django 5.0.1 on 2024-06-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_usertitres_userpostes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postes',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
