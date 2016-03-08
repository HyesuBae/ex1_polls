#-*- coding: utf-8 -*-
from django.contrib import admin
from books.models import Book, Author, Publisher

# Register your models here.
# 여기에 입력하는 이유? admin 사이트에서 보이도록 테이블을 등록해주는 것.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
