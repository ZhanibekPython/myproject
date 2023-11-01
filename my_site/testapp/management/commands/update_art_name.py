from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Updates chosen article'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Enter a pk to get an article')
        parser.add_argument('name', type=str, help='Enter a name')

    def handle(self, *args, **options):
        model1 = apps.get_model('Sem1', 'Article')
        pk = options.get('pk')
        name = options.get('name')
#        article = model1.objects.filter(pk=pk).first()
        article = model1.objects.get(pk=pk)
        article.name = name
        article.save()
        self.stdout.write(f'{article.name}')