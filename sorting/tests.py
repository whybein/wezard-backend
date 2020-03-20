import json
import bcrypt
import jwt

from my_settings import SECRET_KEY
from user.models import User, UserHouse
from .models     import HouseQuestion, HouseChoice, HouseResult, HouseFomula, PassportHouse

from django.test import Client, TestCase


class HouseTest(TestCase):

    def setUp(self):
        User.objects.create(
            id                 = 1,
            email              = 'user@user.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'user',
            last_name          = 'user',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

        HouseQuestion.objects.create(
            id       = 1,
            question = 'question',
        )

        HouseChoice.objects.create(
            id          = 1,
            choice      = 'choice1',
            question_id = 1
        )

        HouseChoice.objects.create(
            id          = 2,
            choice      = 'choice2',
            question_id = 1
        )

    def test_house_get_success(self):
        client   = Client()
        user     = User.objects.get(id=1)
        token    = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        response = client.get(
            '/sorting/house/1',
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'data' : {
                    'id' : 1,
                    'question' : 'question',
                    'img_center' : None,
                    'choices' : [{
                        'id' : 1,
                        'choice' : 'choice1',
                        'img' : None
                    },
                                {
                        'id' : 2,
                        'choice' : 'choice2',
                        'img' : None
                    }]}
            }
        )

    def test_house_get_invalid_keys(self):
        client   = Client()
        user     = User.objects.get(id=1)
        token    = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        response = client.get(
            '/sorting/house/10',
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEYS'
            }
        )

    def test_house_get_login_required(self):
        client   = Client()
        response = client.get('/sorting/house/1')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
            {
                'message' : 'LOGIN_REQUIRED'
            }
        )

class HouseResultTest(TestCase):

    def setUp(self):
        User.objects.create(
            id                 = 1,
            email              = 'user@user.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'user',
            last_name          = 'user',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

        HouseQuestion.objects.create(
            id       = 1,
            question = 'question',
        )

        HouseQuestion.objects.create(
            id       = 2,
            question = 'question',
        )

        HouseQuestion.objects.create(
            id       = 3,
            question = 'question',
        )

        HouseChoice.objects.create(
            id          = 1,
            choice      = 'choice1',
            question_id = 1
        )

        HouseChoice.objects.create(
            id          = 3,
            choice      = 'choice2',
            question_id = 2
        )

        HouseChoice.objects.create(
            id          = 6,
            choice      = 'choice2',
            question_id = 3
        )

        HouseResult.objects.create(
            id             = 1,
            img_bg         = 'img',
            img_icon       = 'img',
            intro          = 'intro',
            message        = 'message',
            name           = 'name',
            person1_img    = 'img',
            person1_name   = 'name',
            person2_img    = 'img',
            person2_name   = 'name',
            person3_img    = 'img',
            person3_name   = 'name',
            person_img_bg  = 'img',
            quotes         = 'quotes',
            share_img_bg   = 'img',
            share_img_icon = 'img',
            tag_line       = 'tag'
        )

        HouseFomula.objects.create(
            id           = 1,
            result_id    = 1,
            question1_id = 1,
            question2_id = 3,
            question3_id = 6
        )

    def test_house_result_post_success(self):
        client = Client()
        user   = User.objects.get(id=1)
        token  = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        data   = {
            'answer_house' : [1,3,6]
        }
        response = client.post(
            '/sorting/house/result',
            json.dumps(data),
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'data':
                {
                    'id'             : 1,
                    'name'           : 'name',
                    'img_icon'       : 'img',
                    'img_bg'         : 'img',
                    'tag_line'       : 'tag',
                    'intro'          : 'intro',
                    'share_img_icon' : 'img',
                    'share_img_bg'   : 'img',
                    'person_img_bg'  : 'img',
                    'person1_img'    : 'img',
                    'person1_name'   : 'name',
                    'person2_img'    : 'img',
                    'person2_name'   : 'name',
                    'person3_img'    : 'img',
                    'person3_name'   : 'name',
                    'message'        : 'message',
                    'quotes'         : 'quotes'
                }
            }
        )

    def test_house_result_port_invalid_keys_index_error(self):
        client = Client()
        user   = User.objects.get(id=1)
        token  = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        data   = {
            'answer_house' : [3,4,6]
        }
        response = client.post(
            '/sorting/house/result',
            json.dumps(data),
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_INDEX'
            }
        )

    def test_house_result_port_invalid_keys_key_error(self):
        client = Client()
        user   = User.objects.get(id=1)
        token  = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        data   = {
            'answer_hous' : [1,4,6]
        }
        response = client.post(
            '/sorting/house/result',
            json.dumps(data),
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEYS'
            }
        )

    def test_house_result_post_login_required(self):
        client   = Client()
        response = client.post(
            '/sorting/house/result',
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
            {
                'message' : 'LOGIN_REQUIRED'
            }
        )

class PssportTest(TestCase):

    def setUp(self):
        User.objects.create(
            id                 = 1,
            email              = 'user@user.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'user',
            last_name          = 'user',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

        User.objects.create(
            id                 = 2,
            email              = 'user2@user.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'user',
            last_name          = 'user',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

        HouseResult.objects.create(
            id   = 1,
            name = 'name'
        )

        HouseResult.objects.create(
            id   = 5,
            name = 'name'
        )

        UserHouse.objects.create(
            user_id         = 1,
            house_result_id = 1
        )

        PassportHouse.objects.create(
            id              = 1,
            house_result_id = 1
        )

        PassportHouse.objects.create(
            id = 5
        )

    def test_passport_get_selected_success(self):
        client   = Client()
        user     = User.objects.get(id=1)
        token    = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        response = client.get(
            '/sorting/passport',
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'data' : {
                    'id' : 1,
                    'house_result' : 1,
                    'img_icon' : None,
                    'img_bg' : None,
                    'img_profile' : None
                },
                'user' : {
                    'first_name' : 'user',
                    'last_name' : 'user'
                }
            }
        )

    def test_passport_get_not_selected_success(self):
        client   = Client()
        user     = User.objects.get(id=2)
        token    = jwt.encode({'user' : user.id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        response = client.get(
            '/sorting/passport',
            **{'HTTP_Authorization':token,
               'content_type' : 'applications/json'
               }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'data' : {
                    'id' : 5,
                    'house_result' : None,
                    'img_icon' : None,
                    'img_bg' : None,
                    'img_profile' : None
                },
                'user' : {
                    'first_name' : 'user',
                    'last_name' : 'user'
                }
            }
        )

    def test_passport_get_login_required(self):
        client   = Client()
        response = client.get('/sorting/passport')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
            {
                'message' : 'LOGIN_REQUIRED'
            }
        )
