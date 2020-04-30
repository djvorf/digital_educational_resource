from django.db import models
from django.urls import reverse


class Lector(models.Model):
    '''Лекция'''
    numberPart = models.CharField("Номер главы", max_length=60, default='null')
    shortInfo = models.TextField("Краткая информация", max_length=500, default='null')
    name = models.CharField("Название лекции", max_length=200)
    content = models.TextField("Содержание")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lector_detail", kwargs={"slug": self.url})

    class Meta():
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"

class Reviews(models.Model):
    '''Отзывы'''
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5009)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class LectorImages(models.Model):
    '''Картинки'''
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", default=None)
    image = models.ImageField("Изображение", upload_to="lector_image/")
    lector = models.ForeignKey(Lector, verbose_name="Лекция", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"