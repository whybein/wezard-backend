from .models import (
    Quiz,
    QuizQuestion,
    QuizChoice,
    QuizResultMessage
)

from django.views import View
from django.http import JsonResponse

class QuizView(View):
    def get(self, request):
        quiz = [
            {
                'title' : quiz.title,
                'author' : quiz.author,
                'img_url' : quiz.img_url,
            }for quiz in Quiz.objects.filter()
        ]
        return JsonResponse({'data': list(quiz)}, status = 200)

class QuizStartView(View):
    def get(self, request):
        quiz_id = request.GET.get('quiz_id', None)
        quiz = Quiz.objects.get(id=quiz_id)
        quiz_start = {
                'id':quiz.id,
                'title' : quiz.title,
                'author' : quiz.author,
                'img_url' : quiz.img_url,
                'description':quiz.description,
                'img_start':quiz.img_start,
                'created_at':quiz.created_at,
                'sorting_quiz':[{
                    'id' : question.id,
                    'question':question.question,
                    'answer':question.answer,
                    'img_url':question.img_url,
                    'quiz_question':[{
                        'id':choice.id,
                        'choice':choice.choice
                    }for choice in QuizChoice.objects.select_related('quiz_question').filter(quiz_question__id=question.id)]
                }for question in QuizQuestion.objects.filter(sorting_quiz_id=quiz.id)]}
        return JsonResponse({'data':quiz_start}, status = 200)