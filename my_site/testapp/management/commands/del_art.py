from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes an article'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Enter a pk to delete an article')

    def handle(self, *args, **options):
        model1 = apps.get_model('Sem1', 'Article')
        pk = options.get('pk')
        article = model1.objects.filter(pk=pk).first()
        if article is not None:
            article.delete()
        self.stdout.write(f'{article}')