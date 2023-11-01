from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Returns an article'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Enter a pk to get an article')

    def handle(self, *args, **options):
        model1 = apps.get_model('Sem1', 'Article')
        pk = options.get('pk')
#        article = model1.objects.filter(pk=pk).first()
        article = model1.objects.get(pk=pk)
        self.stdout.write(f'{article}')