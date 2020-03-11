import json
import bcrypt
import jwt

from .models                import User
from my_settings            import SECRET_KEY

from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.db              import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validate(password):
    validate_condition = [
        lambda s : any(x.isupper() for x in s),
        lambda s : any(x.islower() for x in s),
        lambda s : any(x.isdigit() for x in s),
        lambda s : len(s) >= 8
    ]
    is_password_valid = True
    for validator in validate_condition:
        if not validator(password):
            return False
    return is_password_valid

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate(data['password']):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)

            validate_email(data['email'])

            User(
                email              = data['email'],
                password           = bcrypt.hashpw(
                    data['password'].encode('utf-8'),
                    bcrypt.gensalt()).decode('utf-8'),
                first_name         = data['first_name'],
                last_name          = data['last_name'],
                date_of_birth      = data['date_of_birth'],
                is_send_newsletter = data['is_send_newsletter']
            ).save()

            return HttpResponse(status = 200)

        except IntegrityError:
            return JsonResponse({"message" : "DUPLICATED_EMAIL"}, status = 400)

        except ValidationError:
            return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({"user":user.email}, SECRET_KEY['secret'], algorithm = 'HS256')

                    return JsonResponse({"token" : token.decode('utf-8')}, status = 200)

                return JsonResponse({"message" : "NO_MATCHING_INFO"}, status = 401)

            return JsonResponse({"message" : "NO_MATCHING_INFO"}, status = 400)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)
