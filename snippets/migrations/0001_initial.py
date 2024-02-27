# Generated by Django 4.2.10 on 2024-02-24 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['car_name'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='snippets.car')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
