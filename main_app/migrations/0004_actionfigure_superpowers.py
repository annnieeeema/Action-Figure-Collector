# Generated by Django 4.0.6 on 2022-07-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_superpower_alter_movie_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionfigure',
            name='superpowers',
            field=models.ManyToManyField(to='main_app.superpower'),
        ),
    ]
