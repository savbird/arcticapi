# Generated by Django 3.0.3 on 2020-02-28 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_product_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]