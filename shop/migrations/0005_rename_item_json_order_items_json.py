# Generated by Django 3.2.4 on 2021-07-03 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item_json',
            new_name='items_json',
        ),
    ]
