# Generated by Django 3.1.2 on 2021-03-03 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0028_useproductsheet_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useproductsheetproducts',
            name='use_product_sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_product_sheet_productss', to='mainApp.useproductsheet'),
        ),
    ]
