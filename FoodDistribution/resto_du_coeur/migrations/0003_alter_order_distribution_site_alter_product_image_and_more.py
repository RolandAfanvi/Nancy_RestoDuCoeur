# Generated by Django 5.0.2 on 2024-03-10 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification_app', '0001_initial'),
        ('resto_du_coeur', '0002_remove_product_stock_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='distribution_site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification_app.distributionsite'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.DeleteModel(
            name='DistributionSite',
        ),
    ]
