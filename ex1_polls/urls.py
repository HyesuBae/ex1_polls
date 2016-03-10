from django.conf.urls import include, url
from django.contrib import admin
from ex1_polls import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ex1_polls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls', namespace="books")),
]
