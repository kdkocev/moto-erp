# Generated by Django 2.2.17 on 2021-02-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(),
        ),
    ]
