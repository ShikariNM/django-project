from django.core.management.base import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    help = "Deletes a product from the database by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product} has been deleted')
