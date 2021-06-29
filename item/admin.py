from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ['image_tag','name','price','is_active']
   # list_display = [field.name for field in Categories._meta.fields]
    list_filter = ('line',)


    # readonly_fields = ('order_code',  'total_price',  'created_tag')
    #include = ['created_at']
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = Item

admin.site.register(Item,ItemAdmin)
