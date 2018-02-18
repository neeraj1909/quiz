from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

class Question(TimeStampedModel):
	html = models.TextField(_('Question Text'))

	def __str__(self):
		return self.html


class Choice(TimeStampedModel):
	question = models.ForeignKey(Question, related_name = 'choices', on_delete = models.CASCADE)
	html = models.TextField(_('Choice Text'))

	def __str__(self):
		return self.html