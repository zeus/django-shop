from django.db import models

from shop.models.productmodel import Product
from shop.util.fields import CurrencyField


class BookProduct(Product):
    class Meta(object):
        app_label = 'project'

    isbn = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()


class CompactDiscProduct(Product):
    class Meta(object):
        app_label = 'project'

    number_of_tracks = models.IntegerField()


class BaseProduct(models.Model):
    class Meta(object):
        app_label = 'project'

    unit_price = CurrencyField()


class ProductVariation(Product):
    class Meta(object):
        app_label = 'project'
        
    baseproduct = models.ForeignKey(BaseProduct)

    def get_price(self):
        return self.baseproduct.unit_price


