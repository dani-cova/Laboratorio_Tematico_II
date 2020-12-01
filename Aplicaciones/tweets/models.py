from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoría',max_length = 100, null = False,blank = False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class COVID_19(models.Model):
    id = models.AutoField(primary_key = True)
    UserName = models.CharField('UserName',max_length = 8, null = False, blank = False)
    ScreenName = models.CharField('ScreenName',max_length = 10, null = False, blank = False)
    Location = models.CharField('Location', max_length = 50, null = True, blank = True)
    TweetAt = models.DateField('TweetAt', auto_now = False,auto_now_add = True)
    OriginalTweet = models.CharField('OriginalTweet',max_length = 80000, null = False, blank = False)
    cat = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('public/No-public', default = True)
    Sentiment = models.CharField('Sentiment (Neutral, Positive, Extremely Negative, Negative)',max_length = 25, null = False, blank = False)
    
class Meta:
    verbose_name = 'COVID_19'
    verbose_name_plural = 'COVID_19s'

def _str_(self):
    return "{0},{1}".format(self.ScreenName, self.UserName)


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 90, blank = False, null = False)
    slug = models.CharField('slug', max_length = 100, blank= False, null = False)
    descripcion = models.CharField('descripcion', max_length =110,blank= False, null = False )
    cotenido = RichTextField()
    imagen = models.URLField(max_length = 255, blank= False, null = False)
    COVID_19 = models.ForeignKey(COVID_19, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('public/No-public', default = True)
    fechaCre = models.DateField('fechaCre', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def _str_(self):
        return self.titulo


# Create your models here.
