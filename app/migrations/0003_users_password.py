# Generated by Django 5.0.1 on 2024-05-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_centreinterets_competences_experiencespro_formations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='', max_length=250),
        ),
    ]