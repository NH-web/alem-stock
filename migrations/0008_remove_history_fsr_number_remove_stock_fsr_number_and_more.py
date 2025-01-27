# Generated by Django 5.1.1 on 2024-12-23 11:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manage', '0007_alter_stock_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='fsr_number',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='fsr_number',
        ),
        migrations.AddField(
            model_name='history',
            name='fs_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='issue_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='targa_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='fs_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='issue_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='targa_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='beg_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='history',
            name='onhand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='history',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='beg_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='onhand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
