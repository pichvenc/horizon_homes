# Generated by Django 4.2.7 on 2023-11-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]