# Generated by Django 5.1.1 on 2024-12-18 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manage', '0004_alter_stock_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='reorder_level',
            new_name='beg_quantity',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='issue_to',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='measure',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='receive_by',
        ),
        migrations.AddField(
            model_name='stock',
            name='fsr_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='onhand',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='purch_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sales_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('beg_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('purch_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('sales_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('onhand', models.IntegerField(blank=True, default=0, null=True)),
                ('fsr_number', models.IntegerField(blank=True, default=0, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('issue_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock_manage.category')),
            ],
        ),
    ]