# Generated by Django 5.0.4 on 2025-03-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.IntegerField()),
                ('password', models.IntegerField()),
            ],
        ),
    ]
