# Generated by Django 5.2.2 on 2025-06-08 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="factory",
            name="debt_to_supplier",
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="factory",
            name="supplier",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="network.supplier"
            ),
        ),
        migrations.AlterField(
            model_name="individualentrepreneur",
            name="debt_to_supplier",
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="retailnetwork",
            name="debt_to_supplier",
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="retailnetwork",
            name="supplier",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="network.factory"
            ),
        ),
    ]
