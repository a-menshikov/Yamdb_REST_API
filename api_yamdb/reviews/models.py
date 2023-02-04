from django.db import models

from user.models import User


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='Псевдоним категории',
    )

    def __str__(self):
        """Возвращает слаг категории."""
        return f'{self.slug}'


class Genre(models.Model):
    """Модель жанра."""

    name = models.CharField(max_length=256, verbose_name='Название жанра')
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='Псевдоним жанра'
    )

    def __str__(self):
        """Возвращает слаг жанра."""
        return f'{self.slug}'


class Title(models.Model):
    """Модель тайтла."""

    name = models.CharField(max_length=256, verbose_name='Название тайтла')
    year = models.PositiveIntegerField()
    description = models.TextField(verbose_name='Описание тайтла')
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
    )
    category = models.ForeignKey(
        Category,
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


class Review(models.Model):
    """Модель ревью (отзывы на произведения)."""

    text = models.TextField(verbose_name='текст ревью')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор',
    )
    score = models.PositiveIntegerField(
        verbose_name='оценка',
        #  validators=дописать
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='название произведения',
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращает текст отзыва."""
        return self.text


class Comment(models.Model):
    """Модель комментария."""

    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Aвтор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='oтзыв',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращает текст комментария."""
        return self.text
