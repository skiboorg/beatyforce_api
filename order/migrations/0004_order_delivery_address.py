# Generated by Django 3.2.4 on 2021-07-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderstatus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес доставки'),
        ),
    ]
