from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('rand_num/', views.rand_num, name='randnum'),
    path('stats/<int:num>', views.stats, name='stats'),
    path('add_art/<str:name>/<str:body>/<str:author>/<str:category>/', views.add_art, name='add_art'),
    path('upload/', views.add_image, name='add_image'),
    path('author_arts/', views.get_arts_author, name='author_articles'),
    path('get_article/<int:art_id>', views.get_article, name='get_article'),
    path('choose_game/', views.choose_game, name='choose_game'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_article/', views.add_article, name='add_article'),
    path('update_prod/<int:product_pk>', views.update_production, name='update_prod'),
]
