# Generated by Django 4.1.2 on 2022-10-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="products/%Y/%m/%d"),
        ),
    ]
