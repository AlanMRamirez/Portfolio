# Generated by Django 4.0.6 on 2022-07-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infoabout',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AddField(
            model_name='infoabout',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]