import json
import jwt
import bcrypt

from .models     import User
from my_settings import SECRET_KEY

from django.test import Client, TestCase

class SignUpTest(TestCase):

    def setUp(self):
        User.objects.create(
            email              = 'dup@dup.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'dup',
            last_name          = 'dup',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signupview_post_success(self):
        client = Client()
        user = {
            'email'              : 'post@post.com',
            'password'           : 'weWe1234',
            'first_name'         : 'post',
            'last_name'          : 'post',
            'date_of_birth'      : '1999-12-31',
            'is_send_newsletter' : True
        }
        response = client.post(
            '/user/sign-up',
            json.dumps(user),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_signupview_post_duplicated_email(self):
        client = Client()
        user = {
            'email'              : 'dup@dup.com',
            'password'           : 'weWe1234',
            'first_name'         : 'post',
            'last_name'          : 'post',
            'date_of_birth'      : '1999-12-31',
            'is_send_newsletter' : True
        }
        response = client.post(
            '/user/sign-up',
            json.dumps(user),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'DUPLICATED_EMAIL'
            }
        )

    def test_signupview_post_invalid_password(self):
        client = Client()
        user = {
            'email'              : 'invalid@pass.com',
            'password'           : 'wewe1234',
            'first_name'         : 'post',
            'last_name'          : 'post',
            'date_of_birth'      : '1999-12-31',
            'is_send_newsletter' : True
        }
        response = client.post(
            '/user/sign-up',
            json.dumps(user),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_PASSWORD'
            }
        )

    def test_signupview_post_invalid_email(self):
        client = Client()
        user = {
            'email'              : 'email.com',
            'password'           : 'weWe1234',
            'first_name'         : 'post',
            'last_name'          : 'post',
            'date_of_birth'      : '1999-12-31',
            'is_send_newsletter' : True
        }
        response = client.post(
            '/user/sign-up',
            json.dumps(user),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_EMAIL'
            }
        )

    def test_signupview_post_invalid_keys(self):
        client = Client()
        user = {
            'mail'               : 'email.com',
            'password'           : 'weWe1234',
            'first_name'         : 'post',
            'last_name'          : 'post',
            'date_of_birth'      : '1999-12-31',
            'is_send_newsletter' : True
        }
        response = client.post(
            '/user/sign-up',
            json.dumps(user),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEYS'
            }
        )

class SignInTest(TestCase):

    def setUp(self):
        User.objects.create(
            email              = 'sign@in.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'sign',
            last_name          = 'in',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True

        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signinview_post_success(self):
        client = Client()
        user = {
            'email'    : 'sign@in.com',
            'password' : 'weWe1234'
        }
        response = client.post(
            '/user/sign-in',
            json.dumps(user),
            content_type = 'applications/json'
        )
        token = jwt.encode({"user":user['email']}, SECRET_KEY['secret'], algorithm = 'HS256')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'token' : token.decode('utf-8')
            }
        )

    def test_signinview_post_wrong_password(self):
        client = Client()
        user = {
            'email'    : 'sign@in.com',
            'password' : 'wewe1234'
        }
        response = client.post(
            '/user/sign-in',
            json.dumps(user),
            content_type='applications/json'
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
            {
                'message' : 'NO_MATCHING_INFO'
            }
        )

    def test_signinview_post_wrong_email(self):
        client = Client()
        user = {
            'email'    : 'sagn@in.com',
            'password' : 'weWe1234'
        }
        response = client.post(
            '/user/sign-in',
            json.dumps(user),
            content_type='applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'NO_MATCHING_INFO'
            }
        )

    def test_signinview_post_INVALID_KEYS(self):
        client = Client()
        user = {
            'mail'    : 'sign@in.com',
            'password' : 'wewe1234'
        }
        response = client.post(
            '/user/sign-in',
            json.dumps(user),
            content_type='applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEYS'
            }
        )

class EmailCheckTest(TestCase):

    def setUp(self):
        User.objects.create(
            email              = 'dupl@dupl.com',
            password           = bcrypt.hashpw(
                'weWe1234'.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8'),
            first_name         = 'sign',
            last_name          = 'in',
            date_of_birth      = '1999-12-31',
            is_send_newsletter = True
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_emailcheckview_post_success(self):
        client = Client()
        data = {
            'email' : 'post@post.com',
        }
        response = client.post(
            '/user/email-check',
            json.dumps(data),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_emailcheckview_post_duplicated_email(self):
        client = Client()
        data = {
            'email' : 'dupl@dupl.com',
        }
        response = client.post(
            '/user/email-check',
            json.dumps(data),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'DUPLICATED_EMAIL'
            }
        )

    def test_emailcheckview_post_invaild_email(self):
        client = Client()
        data = {
            'email' : 'dupdup.com',
        }
        response = client.post(
            '/user/email-check',
            json.dumps(data),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_EMAIL'
            }
        )

    def test_emailcheckview_post_invaild_keys(self):
        client = Client()
        data = {
            'emai' : 'dupdup.com',
        }
        response = client.post(
            '/user/email-check',
            json.dumps(data),
            content_type = 'applications/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEYS'
            }
        )
