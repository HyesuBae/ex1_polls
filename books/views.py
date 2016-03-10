#-*- coding: utf-8 -*-
from django.shortcuts import render

# Generic View import
# Generic View란? 장고에서 웹 프로그램 개발 시 공통적으로 사용할 수 있는 로직을
# 미리 개발해놓고 제공하는 뷰
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# 특별한 로직이 없고 템플릿 파일만을 렌더링하는 경우에는 TemplateView
# 필수적으로 template_name 클래스변수를 오버라이딩해서 지정해줘야한다.
# 템플릿 시스템으로 넘겨줄 컨텍스트 변수가 있을 땐 get_context_data() 메소드를 오버라이딩
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    # as_view(), dispatch() 함수는 장고에서 기본적으로 제공.
    # 정확히는, View 클래스에 구현되어 있고, 다른 뷰들은 이 클래스를 inherit하기 때문에
    # 이 함수들도 당연히 상속받는 것.
    # as_view() : 진입 메소드. 클래스의 인스턴스 생성, 그 인스턴스의 dispatch() 메소드 호출
    # dispatch() : request를 검사해서 GET, POST 등의 어떤 HTTP메소드로 요청되었는지
    #       알아낸 다음, 인스턴스 내에서 해당 이름을 갖는 메소드로 요청을 중계해 준다.
    #       해당 메소드가 정의되어있찌 않으면 HttpResponseNotAllowed Exception

    def get_context_data(self, **kwargs):
        # 이 메소드를 오버라이딩할 떈 반드시 첫 줄에 super 오버라이딩 해야함
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        # return 필수
        return context

# ListView를 상속받는 경우는 객체가 들어있는 리스트를 구성해서
# 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 된다.
# 테이블에 들어있는 모든 레코드를 가져와서 리스트를 구성하고 싶으면 모델 클래스명(즉 테이블명)
# 만 지정해주면 된다.
# 장고에서는 명시적으로 지정하지 않아도 디폴트로 속성(attribute)을 지정해준다.
# 1) 컨텍스트 변수명 : object_list
# 2) 템플릿 파일 : 모델명소문자_list.html
class BookList(ListView):
    model = Book
    # 즉 여기서는, Book 테이블로부터 모든 레코드를 가져와서 object_list라는 컨텍스트 변수를
    # 구성하고, 템플릿 파일은 디폴트로 books/book_list.html 파일이 된다.
    # !??? 여기서 books/는 왜 붙음?

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher


# DetailView는 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 된다.
# 만약 테이블에서 prmary key로 조회해서 특정 객체를 가져오는 경우에는 모델 클래스명만
# 지정해주면 된다. 조회 시 사용할 primary key는 URLconf (urls.py ?)에서 추출해서
# 뷰로 넘어온 파라미터를 사용한다.
# 장고에서 지정해주는 디폴트 속성
# 1) 컨텍스트 변수명 : object
# 2) 템플릿 파일명 : 모델명소문자_detail.html
class BookDetail(DetailView):
    model = Book
    # 즉, Book 테이블로부터 특정 레코드를 가져와서 object라는 컨텍스트 변수 구성.
    # 템플릿 파일은 디폴트로 books/book_detail.html
    # 테이블 조회 조건에 사용되는 primary key는 URLconf에서 넘겨받는데,
    # 이에 대한 처리는 DetailView 에서 알아서 처리해줌. 오오?

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher
