# Generated by Django 4.0.5 on 2022-06-09 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbt', '0006_alter_contract_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('value_amount', models.IntegerField()),
                ('person', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbt.contract')),
            ],
        ),
        migrations.CreateModel(
            name='BillingRevenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('billinged_person', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=50)),
                ('value_amount', models.IntegerField()),
                ('client', models.CharField(max_length=30)),
                ('client_manager', models.CharField(max_length=5, null=True)),
                ('client_manager_email', models.EmailField(max_length=30, null=True)),
                ('deposit_at', models.DateField()),
                ('account', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbt.contract')),
            ],
        ),
    ]