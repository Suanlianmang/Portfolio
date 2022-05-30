# Generated by Django 4.0.4 on 2022-05-30 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('github', models.CharField(max_length=200)),
                ('site', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
