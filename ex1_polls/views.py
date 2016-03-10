#-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    # Template 파일 위치 디렉토리는 settings.py에 정의되어 있음
    #       django 1.7 이전까지 : TEMPLATE_DIRS
    #       django 1.8         : TEMPLATES -> DIRS !?
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] = ['polls','books']
        return context
