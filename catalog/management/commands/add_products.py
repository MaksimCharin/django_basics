from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавление категории и продуктов'

    def handle(self, *args, **kwargs):
        # Удаление данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка данных
        try:
            call_command('loaddata', 'catalog_fixture.json')
            self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data from fixture: {e}'))