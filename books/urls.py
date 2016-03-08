#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns('',
    url(r'^$', views.BooksModelView.as_view(), name='index'),

    url(r'^book/$', views.BookList.as_view(), name='book_list'),
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'),

    # url의 \d+ 값이 pk라는 변수에 할당되어 as_view() 함수에 인자로 전달됨!?
    url(r'^book/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    url(r'^publisher/(?P<pk>\d+)/$', views.PublisherDetail.as_view(), name='publisher_detail'),

)
