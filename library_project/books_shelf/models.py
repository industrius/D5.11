from django.db import models

class Author(models.Model):
    full_name = models.TextField("Имя автора")
    birth_year = models.SmallIntegerField("Год рожения")
    country = models.CharField("Страна", max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Publisher(models.Model):
    title = models.CharField("Издательство", max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Friend(models.Model):
    full_name = models.TextField("Имя друга")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"


class Book(models.Model):
    """ Книги """
    ISBN = models.CharField("Международный стандартный книжный номер", max_length=13, default="")
    title = models.TextField("Название")
    description = models.TextField("Аннотация")
    year_release = models.PositiveSmallIntegerField("Год издания")
    copy_count = models.PositiveSmallIntegerField("Количество экземпляров", default=1)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    author = models.ForeignKey("books_shelf.Author", on_delete=models.CASCADE, verbose_name="Автор", related_name="book_author")
    publisher = models.ForeignKey("books_shelf.Publisher", on_delete=models.CASCADE, null=True, verbose_name="Издатель", related_name="book_publisher")
    friends = models.ManyToManyField("books_shelf.Friend", verbose_name="Друг", related_name="rented_by_friend", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"