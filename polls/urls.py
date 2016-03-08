#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from polls import views

# patterns() : URL/view mapping을 처리하는 함수.
# url(regex(필수), view(필수), kwargs=None, name=None, prefix='')
# regex : url을 정규표현식으로 표현. 뷰 함수에 넘겨줄 파라미터를 추출할 수 있다.
# view  : 요청의 URL이 regex인자에 매칭되면 장고가 뷰 함수를 호출한다. 뷰 함수에는
#           HttpRequest와 regex에서 추출한 항목을 인자로 넘겨준다.
# kwargs : regex 인자에서 추출한 파라미터 외에 추가적인 인자를
#           dict 타입의 키워드 인자로 뷰 함수에 넘겨줄 수 있다.
# name : 각 url 별로 이름을 붙여준다. 여기서 정한 이름은 템플릿 파일에서 사용된다.
# prefix : 뷰 함수에 대한 접두사 문자열. !?!?
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
)
