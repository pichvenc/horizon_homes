# Generated by Django 4.2.7 on 2023-11-28 03:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('horizon_main', '0004_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]