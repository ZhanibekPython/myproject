from django.contrib import admin

from .models import CategoryAdm, ProductAdm, Coin, Author, Article, Comment, Client, Production, Order

admin.site.register(CategoryAdm)
admin.site.register(ProductAdm)
admin.site.register(Coin)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Client)
admin.site.register(Production)
admin.site.register(Order)