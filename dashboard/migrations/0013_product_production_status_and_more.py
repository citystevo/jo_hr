# Generated by Django 4.2 on 2024-10-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='production_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='production_status_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
