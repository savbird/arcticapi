# Generated by Django 3.0.3 on 2020-02-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_product_prodid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='0', max_length=7),
            preserve_default=False,
        ),
    ]