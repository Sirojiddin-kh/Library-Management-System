from modeltranslation.translator import translator, TranslationOptions
from .models import Book


class BookCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Book, BookCategoryTranslationOptions)