# Generated by Django 3.1.2 on 2021-02-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_getproductsheetproducts_out_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='warehouse',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='mainApp.warehouse'),
        ),
    ]
