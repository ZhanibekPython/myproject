from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates new article'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('body', type=str)
        parser.add_argument('author_name', type=str)
        parser.add_argument('author_surname', type=str)

    def handle(self, *args, **options):
        model1 = apps.get_model('Sem1', 'Article')
        model2 = apps.get_model('Sem1', 'Author')
        name = options.get('name')
        body = options.get('body')
        author_name = options.get('author_name')
        author_surname = options.get('author_surname')
        author = model2(name=author_name, surname=author_surname)
        author.save()
        article = model1(name=name, body=body, author=author)
        article.save()
        self.stdout.write(f'{article}')