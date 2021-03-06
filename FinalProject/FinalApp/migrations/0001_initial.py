# Generated by Django 3.2.1 on 2021-05-05 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('prime_customer', models.CharField(default='N', max_length=1)),
                ('customer_since', models.DateField(default=datetime.datetime(2021, 5, 5, 19, 55, 17, 522029))),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=datetime.datetime(2021, 5, 5, 19, 55, 17, 522029))),
                ('order_total', models.FloatField()),
                ('payment_type', models.CharField(max_length=1)),
                ('account_number', models.CharField(max_length=20)),
                ('expiration_date', models.DateField(default=datetime.datetime(2022, 5, 5, 19, 55, 17, 522029))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=25)),
                ('item_quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalApp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalApp.customer')),
            ],
            options={
                'ordering': ['street'],
            },
        ),
    ]
