from django.db import models





class Cart(models.Model):
    client = models.ForeignKey('user.User', blank=True, null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='Корзина клиента')


    weight = models.IntegerField(default=0)
    raw_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина клиента : {self.client.id} '

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True,null=True, verbose_name='Корзина', db_index=True,related_name='items')

    item = models.ForeignKey('item.Item', blank=True, null=True, on_delete=models.CASCADE, db_index=True)
    quantity = models.IntegerField('Кол-во', blank=True, null=True, default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.item.name}  X {self.quantity}'

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзинах"

    def save(self, *args, **kwargs):
        self.price = self.item.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)