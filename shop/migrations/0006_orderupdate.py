# Generated by Django 3.2.4 on 2021-07-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_item_json_order_items_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
