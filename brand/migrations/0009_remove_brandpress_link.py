# Generated by Django 3.2.4 on 2021-06-28 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0008_brandingredient_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandpress',
            name='link',
        ),
    ]
