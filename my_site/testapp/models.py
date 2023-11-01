from django.db import models


class Coin(models.Model):
    toss = models.CharField(max_length=30)
    time = models.TimeField()

    def _str_(self):
        return f'{self.toss} at {self.time}'

    @staticmethod
    def coinstat(n: int):
        check = Coin.objects.order_by('-time')[:n]
        stats = {'heads': 0, 'tails': 0}
        for throw in check:
            if throw.toss == 'heads':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Author - {self.surname} {self.name}'

    class Meta:
        ordering = ['surname']
        indexes = [
            models.Index(fields=['surname'])
        ]


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=30, default='Risky Johny')
    view = models.IntegerField(default=0, null=True)
    is_publ = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.view += 1
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'Article - {self.name} {self.body}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment - {self.author} for {self.article}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product_photos/')


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    adres = models.CharField(max_length=100, blank=True)
    registartion_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client - {self.name} registered on {self.registartion_date}'


class Production(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quontity = models.PositiveIntegerField(default=0)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    production = models.ManyToManyField(Production)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.total_price}'


class CategoryAdm(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProductAdm(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryAdm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
