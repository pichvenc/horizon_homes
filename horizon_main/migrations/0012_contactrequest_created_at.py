# Generated by Django 4.2.7 on 2023-11-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizon_main', '0011_contactrequest_alter_requestviewing_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]