# Generated by Django 5.1.1 on 2024-12-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manage', '0012_remove_history_onhand_remove_history_purch_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='username',
            new_name='history_category',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='fs_number',
            new_name='history_fs_number',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='beg_quantity',
            new_name='history_issue_quantity',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='last_updated',
            new_name='history_last_updated',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='issue_quantity',
            new_name='history_receive_quantity',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='targa_number',
            new_name='history_targa_number',
        ),
        migrations.RemoveField(
            model_name='history',
            name='category',
        ),
        migrations.RemoveField(
            model_name='history',
            name='issue_to',
        ),
        migrations.RemoveField(
            model_name='history',
            name='receive_quantity',
        ),
        migrations.AddField(
            model_name='history',
            name='history_username',
            field=models.CharField(default='nati', max_length=100),
            preserve_default=False,
        ),
    ]
