# Generated by Django 4.2.7 on 2023-11-28 05:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('horizon_main', '0007_property_country_property_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestViewing',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('preferred_date', models.DateField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horizon_main.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horizon_main.userprofile')),
            ],
        ),
    ]
