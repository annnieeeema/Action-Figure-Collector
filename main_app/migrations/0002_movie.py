# Generated by Django 4.0.6 on 2022-07-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('actionfigure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.actionfigure')),
            ],
        ),
    ]
