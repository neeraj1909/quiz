from django.contrib import admin

from .models import Question, Choice
# Register your models here.
class ChoiceAdmin(admin.TabularInline):
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	model = Question
	inlines = (ChoiceAdmin, )

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)