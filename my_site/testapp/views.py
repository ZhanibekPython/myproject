import logging
import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, Choose_game, AddAuthor, AddArticle, UpdateProduction
from .models import Coin, Article, Author, Production

logging.basicConfig(filename='Seminars.log', level=logging.INFO)

logger = logging.getLogger(__name__)

menu = [
    {'name': 'Main page', 'url_name': 'index'},
    {'name': 'Coin game', 'url_name': 'coin'},
    {'name': 'Random nums game', 'url_name': 'randnum'},
]


def index(request):
    data = {'title': 'Start page', 'about': 'Welcome to our web-site', 'menu': menu}
    return render(request, 'testapp/index.html', data)


def coin(request):
    seq = ['heads', 'tails']
    toss = random.choice(seq)
    time = datetime.now()
    attempt = Coin(toss=toss, time=time)
    attempt.save()
    logger.info(f'Coin was tossed and fell on {toss} at {time}')
    data = {
        'time': time,
        'toss': toss,
        'attempt': attempt,
        'menu': menu
    }
    return render(request, 'testapp/coin.html', context=data)


def rand_num(request):
    num = random.randint(1, 101)
    logger.info(f'Random made - {num}')
    return render(request, 'testapp/rand_num.html', context={'menu': menu,
                                                             'title': 'Random nums game',
                                                             'num': num})


def stats(request, num):
    logger.info(f'Statistics page')
    return JsonResponse(Coin.coinstat(num))


def add_art(request, name, body, author, category):
    article = Article(name=name, body=body, author=author, category=category)
    article.save()
    return f'{article}'


def get_arts_author(request):
    articles = Article.objects.all()
    article = Article.objects.all().first()
    data = {'title': 'Author articles page', 'articles': articles,
            'info': 'Все статьи автора', 'article': article}
    return render(request, 'testapp/get_arts_author.html', context=data)


def get_article(request, art_id: int):
    article = get_object_or_404(Article, pk=art_id)
    article.view += 1
    # article.save()
    return render(request, 'testapp/get_article.html',
                  context={'title': 'Check how many views an article has', 'info': article})


def add_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'image_upload.html', {'form': form})


def choose_game(request):
    if request.method == 'POST':
        form = Choose_game(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            attempts = form.cleaned_data['attempts']
            logger.info(f'Была выбрана игра {game} и количество попыток {attempts}')
            if game == 'R':
                return rand_num(request)
            else:
                return coin(request)
    else:
        form = Choose_game()
    return render(request, 'testapp/choose_game.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        message = 'Ошибка ввода данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthdate = form.cleaned_data['birthdate']
            new_author = Author(name=name, surname=surname, email=email,
                                biography=biography, birthdate=birthdate)
            new_author.save()
            message = 'Автор сохранен'
    else:
        form = AddAuthor()
        message = 'Введите данные нового автора'
    return render(request, 'testapp/new_author.html', {'form': form, 'message': message})


def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        message = 'Ошибка ввода данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']
            pub_date = form.cleaned_data['pub_date']
            category = form.cleaned_data['category']
            view = form.cleaned_data['view']
            is_publ = form.cleaned_data['is_publ']
            new_article = Article(name=name, body=body, pub_date=pub_date, category=category,
                                  view=view, is_publ=is_publ)
            new_article.save()
            message = 'Статья сохранена'
    else:
        form = AddArticle()
        message = 'Введите данные новой статьи'
    return render(request, 'testapp/new_article.html', {'form': form, 'message': message})


def update_production(request, product_pk):
    product = get_object_or_404(Production, pk=product_pk)
    if request.method == 'POST':
        form = UpdateProduction(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quontity = form.cleaned_data['quontity']
            product.save()
            return redirect(update_production, product_pk)
    else:
        form = UpdateProduction()
    return render(request, 'testapp/update_prod.html', {'form': form})
