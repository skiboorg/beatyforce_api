from django.db import models
from django.db.models.signals import post_save, post_delete

from item.models import Item
from django.utils.safestring import mark_safe


class OrderStatus(models.Model):
    name = models.CharField('Статус', max_length=10, blank=True, null=True)
    color = models.CharField('Цвет', max_length=10, blank=True, null=True)
    is_default = models.BooleanField('По умалчанию', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"

class Order(models.Model):
    client = models.ForeignKey('user.User', blank=True, null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='Заказ клиента')
    status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='Статус заказа')
    delivery = models.CharField('Тип доставки', max_length=255, blank=True, null=True)
    delivery_address = models.TextField('Адрес доставки', blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)


    total_price = models.IntegerField('Общая стоимость заказа', default=0)

    track_code = models.CharField('Трек код', max_length=50, blank=True, null=True)
    order_code = models.CharField('Код заказа', max_length=10, blank=True, null=True)
    is_complete = models.BooleanField('Заказ выполнен ?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'Заказ № %s. Создан : %s  . Сумма заказа : %s' % (self.id, self.created_at.strftime('%d-%m-%Y'),  self.total_price)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def created_tag(self):
        return mark_safe('<strong>{}</strong>'.format(self.created_at.strftime('%d-%m-%Y, %H:%M:%S')))

    created_tag.short_description = mark_safe('<strong>Дaта заказа</strong>')



class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=False, null=True, default=None, on_delete=models.CASCADE,
                              verbose_name='В заказе',related_name='items')
    item = models.ForeignKey(Item, blank=False, null=True, default=None, on_delete=models.CASCADE,
                              verbose_name='Товар')
    quantity = models.IntegerField('Кол-во', blank=True, null=True, default=0)
    total_price = models.IntegerField('Общая стоимость', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # if self.item.discount > 0:
        #     self.current_price = self.item.price - (self.item.price * self.item.discount / 100)
        # else:
        #     self.current_price = self.item.price
        self.total_price = self.quantity * self.item.price

        super(OrderItem, self).save(*args, **kwargs)


    def __str__(self):
        return 'Товар : %s . В заказе № %s .' % (self.item.name, self.order.id)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"



    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.item.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.item.image.url))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    def name_tag(self):
        name = self.item.name
        return name

    def article_tag(self):
        name = self.item.article
        return name

    article_tag.short_description = 'Артикул'
    name_tag.short_description = 'Название товара'
    image_tag.short_description = 'Основная картинка'


def OrderItemPostSave(sender,instance,**kwargs):
    try:
        order = instance.order
    except:
        order = None

    if order:
        order_total_price = 0
        all_items_in_order = OrderItem.objects.filter(order=order)

        for item in all_items_in_order:
            order_total_price += item.total_price

        instance.order.total_price = order_total_price
        instance.order.save(force_update=True)


post_delete.connect(OrderItemPostSave, sender=OrderItem)
post_save.connect(OrderItemPostSave, sender=OrderItem)
