#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # get_objec_or_404(모델클래스, 검색조건1, 검색조건2, ...)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request,question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST : 제출된 폼의 데이터를 담고 있는 객체.
        #               파이썬의 dict처럼 key로 값을 찾을 수 있다.
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question': p, 'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        # reverse 함수는 url 패턴으로부터 url 스트링을 구한다.
        # 즉 여기서 reverse 함수의 결과는 ex) /polls/3/results/
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
