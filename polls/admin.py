#-*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Question, Choice

# admin web UI에서 question 메뉴를 클릭했을 때 question 뿐만이 아니라
#  choice 목록도 나오고 입력할 수 있도록.
# extra는 기존에 있던 choie 목록 뿐 아니라 추가로 입력할 수 있는
# 빈 choice 칸을 더 보여주는 것.
# admin.StackedInline, admin.TabularInline 등등 다양한 형식으로 UI에 표현가능
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # change order of Questions' fields in admin web UI.
    #fields = ['pub_date', 'question_text']

    # show fields seperately in admin web UI
    # classes : collapse => date information field is fold in admin web UI
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # Choice 모델 클래스 같이 보기
    inlines = [ChoiceInline]

    # record 리스트 항목 지정
    # 즉 ui에서 모델명(테이블 명. 여기서는 Question)을 누르면 나오는
    # 레코드의 목록에서 표시할 항목을 지정.
    list_display = ('question_text', 'pub_date')

    # filter sidebar 추가
    list_filter = ['pub_date']

    # search box
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
