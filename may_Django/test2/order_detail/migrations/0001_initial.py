# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 06:32
from __future__ import unicode_literals

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
                ('CustomerId', models.IntegerField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=10)),
                ('CustomerAddr', models.CharField(max_length=50)),
                ('CustomerCity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discount', models.IntegerField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderTable',
            fields=[
                ('OrderId', models.IntegerField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('CustomerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_detail.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductId', models.IntegerField(primary_key=True, serialize=False)),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ProductName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='OrderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_detail.OrderTable'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='ProductId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_detail.Product'),
        ),
    ]
