# Generated by Django 3.2.4 on 2021-06-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='По умалчанию'),
        ),
    ]