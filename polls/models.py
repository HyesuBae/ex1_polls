#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Question(models.Model): # Database table
	# each variables is matched to column in Database
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self): #__str__ on python 3
		return self.question_text

class Choice(models.Model):
	# foreign key는 Question model의 primary key를 foreign key로 가진다.
	# django 에서 model의 primary key는 autoincrement int값으로 자동으로 설정됨.
	# 즉 여기서는 퀘스천 모델의 자동으로 생성된 프라이머리키를 외래키로 갖는 것.
	question_id = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	# admin web ui에서 보이는 레코드의 제목값을 리턴
	def __unicode__(self):
		return self.choice_text
