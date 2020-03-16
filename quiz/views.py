from .models import Article

from django.views import View
from django.http import JsonResponse

class QuizView(View):
    def get(self, request):
        quiz_list = [
            {
                'title' : quiz.title,
                'author' : quiz.author,
                'img_url' : quiz.img_url,
                # 'description':quiz.discription
            }for quiz in Quiz.objects.filter(article_types__id=1)
        ]
        return JsonResponse({'data': news_list}, status = 200)
