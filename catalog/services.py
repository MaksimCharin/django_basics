from .models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

class ProductService:

    @staticmethod
    def get_products_in_category(category_id):
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def get_products_from_cache():
        if not CACHE_ENABLED:
            return Product.objects.all()
        key='products_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products, 60 * 15)
        return products


class CategoryService:

    @staticmethod
    def get_category_from_cache():
        if not CACHE_ENABLED:
            return Category.objects.all()
        key='category'
        category = cache.get(key)
        if category is not None:
            return category
        category = Category.objects.all()
        cache.set(key, category, 60 * 15)
        return category



