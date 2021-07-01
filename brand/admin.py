from django.contrib import admin
from .models import *
from item.models import Item

class ItemLineInline (admin.TabularInline):
    model = BrandItemLine
    extra = 0


class BrandAdmin(admin.ModelAdmin):
    inlines = [ItemLineInline]
    class Meta:
        model = Brand

class ItemInline (admin.TabularInline):
    fields = ('image_tag','name','price','image',)
    readonly_fields = ('image_tag',)
    model = Item
    extra = 0

class BrandItemLineAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ('brand',)
    inlines = [ItemInline]

    class Meta:
        model = BrandItemLine

admin.site.register(Brand,BrandAdmin)
admin.site.register(BrandItemLine)
admin.site.register(BrandCategory)
admin.site.register(BrandCountry)
admin.site.register(BrandPress)
admin.site.register(BrandFeedback)
admin.site.register(BrandFeature)
admin.site.register(BrandIngredient)
admin.site.register(BrandVideo)
admin.site.register(BrandGlobalCategory)
admin.site.register(Banner)
admin.site.register(Video)
admin.site.register(PressCategory)
admin.site.register(Press)
