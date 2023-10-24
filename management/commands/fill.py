from django.core.management import BaseCommand

from catalog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()


        categories = [
            { 'id':1, 'name': "Бытовая техника",'description': "Техника для дома" },
            { 'id':2, 'name': "Гаджеты",'description': "Смартфоны, телефоны, плееры" },
            {'id': 3, 'name': "Компьютеры", 'description': "Компьютеры и ноутбуки"},
            {'id': 4, 'name': "Телевизоры", 'description': "Теле и аудио системы"},
            {'id': 5, 'name': "Уход и красота", 'description': "Все для красоты"},
        ]

        category_to_fill = []
        for category in categories:
            category_to_fill.append(Category(**category))


        Category.objects.bulk_create(category_to_fill)