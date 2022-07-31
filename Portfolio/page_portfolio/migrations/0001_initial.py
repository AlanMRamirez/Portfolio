# Generated by Django 4.0.6 on 2022-07-25 21:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMiniature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='projects')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.SmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=80)),
                ('description', ckeditor.fields.RichTextField()),
                ('technologies', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project_miniature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_portfolio.projectminiature')),
            ],
        ),
    ]
