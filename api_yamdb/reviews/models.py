from django.db import models


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(max_length=256,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Псевдоним категории')

    def __str__(self):
        """Возвращает слаг категории."""
        return f'{self.slug}'


class Genre(models.Model):
    """Модель жанра."""
    name = models.CharField(max_length=256,
                            verbose_name='Название жанра')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Псевдоним жанра')

    def __str__(self):
        """Возвращает слаг жанра."""
        return f'{self.slug}'


class Title(models.Model):
    """Модель тайтла."""
    name = models.CharField(max_length=256,
                            verbose_name='Название тайтла')
    year = models.PositiveIntegerField()
    description = models.TextField(verbose_name='Описание тайтла')
    genre = models.ManyToManyField(Genre,
                                   through='GenreTitle',
                                   )
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name='category',
                                 verbose_name='Категория тайтла',
                                 )

    def __str__(self):
        """Возвращает название тайтла."""
        return f'{self.name}'


class GenreTitle(models.Model):
    """Связь жанра и тайтла."""
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    title = models.ForeignKey(Title, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} {self.genre}'
