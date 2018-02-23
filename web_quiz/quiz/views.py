from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import QuizProfile, Question, AttemptedQuestion


def home(request):
    context = {}
    return render(request, 'quiz/home.html', context=context)


@login_required()
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)
    question = quiz_profile.get_new_question()

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')
        question =get_object_or_404(Question, pk=question_pk)
        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        context={
            'question': question,
            'selected_choice': selected_choice,
        }

        return render(request, 'quiz/submission_result.html',context)

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)

        context={
            'question': question,
        }

        return render(request, 'quiz/play.html', context=context)

