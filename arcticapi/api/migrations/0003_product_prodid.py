# Generated by Django 3.0.3 on 2020-02-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prodid',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
    ]
