from django.contrib import admin
from .models import Book, Author, Category, Language
# Register your models here.


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    search_fields = ('first_name',)


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Language)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)