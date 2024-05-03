from django.core.management.base import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    help = "Get a product  by id from the database"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
