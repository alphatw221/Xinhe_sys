# Generated by Django 3.1.2 on 2021-02-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_auto_20210225_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='getproductsheetproducts',
            name='out_warehouse',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_productss', to='mainApp.warehouse'),
        ),
    ]
