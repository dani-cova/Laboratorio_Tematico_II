from django.contrib import admin

from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource

class COVID_19Resource(resources.ModelResource):
    class Meta:
        model = COVID_19

class COVID_19Admin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['UserName']
    list_display = ('UserName','ScreenName','Location','TweetAt','OriginalTweet','Sentiment',)
    resource_class = COVID_19Resource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(COVID_19,COVID_19Admin)
admin.site.register(Post)

# Register your models here.
