from .models import(
    HouseChoice,
)

from django.views import View
from django.http  import JsonResponse

class HouseView(View):
    def get(self, request, question_id):
        choice = HouseChoice.objects.select_related('question').filter(question_id = question_id)
        data = {
            'id'         : choice[0].question.id,
            'question'   : choice[0].question.question,
            'img_center' : choice[0].question.img_center,
            'choices'    : list(choice.values('choice', 'img'))
        }

        return JsonResponse({"data" : data}, status = 200)
