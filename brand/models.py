from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from random import choices
import string

class BrandCountry(models.Model):
    name = models.CharField('Страна', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)


    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(BrandCountry, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"




class BrandCategory(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)

    name = models.CharField('Категория бренда', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)

    product_line = models.TextField('Линейка товаров', blank=True, null=True)

    is_active = models.BooleanField('Активный?', default=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(BrandCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class BrandFeature(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    name = models.CharField('Преймущество бренда', max_length=255, blank=True, null=True)
    text = models.TextField('Тест', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Преймущество бренда"
        verbose_name_plural = "Преймущества бренда"


class BrandIngredient(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    name = models.CharField('Ингридиент', max_length=255, blank=True, null=True)
    text = models.TextField('Тест', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Состав и ингредиенты"
        verbose_name_plural = "Состав и ингредиенты"


class BrandFeedback(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    avatar = models.ImageField('Аватар', upload_to='brand/feedback/', blank=True)
    name = models.CharField('ФИО', max_length=255, blank=True, null=True)
    rating = models.IntegerField('Оценка', default=5)
    text = models.TextField('Тест', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class BrandVideo(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    image = models.ImageField('Картинка', upload_to='brand/video/', blank=True)
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    link = models.IntegerField('Код видео', default=5)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class BrandPress(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    logo = models.ImageField('Лого', upload_to='brand/press/logo', blank=True)
    image = models.ImageField('Картинка', upload_to='brand/press/image', blank=True)
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    link = models.IntegerField('Ссылка', default=5)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Пресса"
        verbose_name_plural = "Пресса"

class Brand(models.Model):
    category = models.ManyToManyField(BrandCategory, verbose_name='Категории',
                                  blank=True, db_index=True)
    order_num = models.IntegerField('Порядок вывода', default=100)
    logo = models.ImageField('Логотип', upload_to='brand/logo/', blank=True)
    image = models.ImageField('Изображение для страницы', upload_to='brand/image/', blank=True)
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    is_show_at_index = models.BooleanField('На главной?', default=False)
    is_active = models.BooleanField('Активный?', default=True)

    slogan = models.CharField('Слоган', max_length=255, blank=True, null=True)
    country = models.ForeignKey(BrandCountry, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name='Страна')
    assortiment = models.TextField('Ассортимент', blank=True, null=True)
    prices = models.CharField('Ценовой сегмент', max_length=255, blank=True, null=True)

    description = RichTextUploadingField('Описание', blank=True, null=True)
    description_image = models.ImageField('Изображение для описания', upload_to='brand/image/', blank=True)

    features = models.ManyToManyField(BrandFeature, verbose_name='Преймущества', blank=True)
    features_image = models.ImageField('Изображение для преймуществ', upload_to='brand/image/', blank=True)

    ingredients = models.ManyToManyField(BrandIngredient, verbose_name='Состав и ингредиенты', blank=True)
    feedbacks = models.ManyToManyField(BrandFeedback, verbose_name='Отзывы', blank=True)
    videos = models.ManyToManyField(BrandVideo, verbose_name='Видео', blank=True)
    press = models.ManyToManyField(BrandPress, verbose_name='Пресса', blank=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class BrandGlobalCategory(models.Model):
    order_num = models.IntegerField('Порядок вывода', default=100)
    brands = models.ManyToManyField(Brand,blank=True,verbose_name='Бренды')
    name = models.CharField('Глобальная категория бренда', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(BrandGlobalCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        # ordering = ('order_num',)
        verbose_name = "Глобальная категория"
        verbose_name_plural = "Глобальные категория"