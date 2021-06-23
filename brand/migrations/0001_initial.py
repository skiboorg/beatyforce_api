# Generated by Django 3.2.4 on 2021-06-22 09:14

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Категория бренда')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('product_line', models.TextField(blank=True, null=True, verbose_name='Линейка товаров')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='BrandCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='BrandFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преймущество бренда')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Преймущество бренда',
                'verbose_name_plural': 'Преймущества бренда',
            },
        ),
        migrations.CreateModel(
            name='BrandFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('avatar', models.ImageField(blank=True, upload_to='brand/feedback/', verbose_name='Аватар')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('rating', models.IntegerField(default=5, verbose_name='Оценка')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='BrandIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ингридиент')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Состав и ингредиенты',
                'verbose_name_plural': 'Состав и ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='BrandPress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('logo', models.ImageField(blank=True, upload_to='brand/press/logo', verbose_name='Лого')),
                ('image', models.ImageField(blank=True, upload_to='brand/press/image', verbose_name='Картинка')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('link', models.IntegerField(default=5, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Пресса',
                'verbose_name_plural': 'Пресса',
            },
        ),
        migrations.CreateModel(
            name='BrandVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('image', models.ImageField(blank=True, upload_to='brand/video/', verbose_name='Картинка')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('link', models.IntegerField(default=5, verbose_name='Код видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=100, verbose_name='Порядок вывода')),
                ('logo', models.ImageField(blank=True, upload_to='brand/logo/', verbose_name='Логотип')),
                ('image', models.ImageField(blank=True, upload_to='brand/image/', verbose_name='Изображение для страницы')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('is_show_at_index', models.BooleanField(default=False, verbose_name='На главной?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
                ('slogan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Слоган')),
                ('assortiment', models.TextField(blank=True, null=True, verbose_name='Ассортимент')),
                ('prices', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ценовой сегмент')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_image', models.ImageField(blank=True, upload_to='brand/image/', verbose_name='Изображение для описания')),
                ('features_image', models.ImageField(blank=True, upload_to='brand/image/', verbose_name='Изображение для преймуществ')),
                ('category', models.ManyToManyField(blank=True, db_index=True, to='brand.BrandCategory', verbose_name='Категория доступна в городах')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.brandcountry', verbose_name='Страна')),
                ('features', models.ManyToManyField(blank=True, to='brand.BrandFeature', verbose_name='Преймущества')),
                ('feedbacks', models.ManyToManyField(blank=True, to='brand.BrandFeedback', verbose_name='Отзывы')),
                ('ingredients', models.ManyToManyField(blank=True, to='brand.BrandIngredient', verbose_name='Состав и ингредиенты')),
                ('press', models.ManyToManyField(blank=True, to='brand.BrandPress', verbose_name='Пресса')),
                ('videos', models.ManyToManyField(blank=True, to='brand.BrandVideo', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
    ]
