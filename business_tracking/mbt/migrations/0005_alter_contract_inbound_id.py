# Generated by Django 4.0.5 on 2022-06-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbt', '0004_contract_client_manager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='inbound_id',
            field=models.IntegerField(null=True),
        ),
    ]
