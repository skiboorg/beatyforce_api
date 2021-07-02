from django.db import models
from django.utils.safestring import mark_safe
from pytils.translit import slugify
from brand.models import BrandItemLine
from ckeditor_uploader.fields import RichTextUploadingField

class Item(models.Model):
    line = models.ForeignKey(BrandItemLine, verbose_name='Линейка',
                                   on_delete=models.SET_NULL, blank=True, null=True, db_index=True,related_name='items')
    name = models.CharField('Название товара', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True,default='',editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True,db_index=True, editable=False)

    description = RichTextUploadingField('Описание', blank=True, null=True)
    price = models.IntegerField('Цена', blank=True, default=0, db_index=True)
    price_text = models.CharField('Цена текст', max_length=255, blank=True, null=True, db_index=True)
    article = models.CharField('Артикул', max_length=50, blank=True, null=True)
    discount = models.IntegerField('Скидка', default=0)
    image = models.ImageField('Изображение товара', upload_to='images/catalog/items/', blank=True)
    is_active = models.BooleanField('Отображать товар ?', default=True, db_index=True)
    is_present = models.BooleanField('Товар в наличии ?', default=True, db_index=True)
    is_new = models.BooleanField('Товар новинка ?', default=False, db_index=True)
    buys = models.IntegerField(default=0, editable=False)
    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug
        self.name_lower = self.name.lower()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        # ordering = ('order_num',)
        verbose_name = "Tовар"
        verbose_name_plural = "Tовары"
