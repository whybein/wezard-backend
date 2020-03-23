import json

from user.utils  import login_required
from user.models import UserHouse
from .models     import(
    HouseChoice,
    HouseFomula,
    HouseResult,
    PassportHouse,
)

from django.views        import View
from django.http         import JsonResponse
from django.db.models    import Q
from django.forms.models import model_to_dict

class HouseView(View):
    @login_required
    def get(self, request, question_id):
        try:
            choice = (
                HouseChoice
                .objects.select_related('question')
                .filter(question_id = question_id)
                )
            question_house = {
                'id'         : choice[0].question.id,
                'question'   : choice[0].question.question,
                'img_center' : choice[0].question.img_center,
                'choices'    : list(choice.values('id', 'choice', 'img'))
            }

            return JsonResponse({"data" : question_house}, status = 200)

        except IndexError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

class HouseResultView(View):
    @login_required
    def post(self, request):
        try:
            data   = json.loads(request.body)["answer_house"]
            fomula = (
                HouseFomula
                .objects
                .select_related('result')
                .filter(Q(question1_id = data[0])&
                        Q(question2_id = data[1])&
                        Q(question3_id = data[2]))
            )
            UserHouse(
                user_id         = request.user.id,
                house_result_id = fomula[0].result_id
            ).save()

            result_house = HouseResult.objects.get(id=fomula[0].result_id)
            return JsonResponse({"data" : model_to_dict(result_house)}, status = 200)

        except IndexError:
            return JsonResponse({"message" : "INVALID_INDEX"}, status = 400)
        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

class PassportView(View):
    @login_required
    def get(self, request):
        try:
            result_id = UserHouse.objects.get(user_id = request.user.id).house_result_id
            if result_id:
                return JsonResponse({
                    "data" : model_to_dict(PassportHouse.objects.get(house_result_id=result_id)),
                    "user" : {
                        "first_name" : request.user.first_name,
                        "last_name" : request.user.last_name
                    }
                }, status = 200)
            else:
                data = PassportHouse.objects.get(id=5)
                return JsonResponse({
                    "data" : model_to_dict(data),
                    "user" : {
                        "first_name" : request.user.first_name,
                        "last_name" : request.user.last_name
                    }
                }, status = 200)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)
