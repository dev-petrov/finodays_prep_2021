# Generated by Django 3.2.7 on 2021-09-15 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('engine_power', models.FloatField()),
                ('engine_volume', models.FloatField()),
                ('fuel_type', models.CharField(max_length=32)),
                ('transmission', models.CharField(max_length=32)),
                ('drive', models.CharField(max_length=32)),
                ('cylinders_count', models.IntegerField()),
                ('wheel', models.CharField(max_length=32)),
                ('height', models.FloatField()),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('wheel_base', models.FloatField()),
                ('catalog_link', models.URLField()),
                ('eco_class', models.CharField(blank=True, max_length=16, null=True)),
                ('generation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modifications', to='car.generation')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('body_type', models.CharField(max_length=32)),
                ('doors_count', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='models', to='car.brand')),
            ],
        ),
        migrations.AddField(
            model_name='generation',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='generations', to='car.model'),
        ),
    ]
