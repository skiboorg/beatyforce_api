# Generated by Django 3.2.4 on 2021-06-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Отображать товар ?'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_bestseller',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Bestseller ?'),
        ),
    ]
