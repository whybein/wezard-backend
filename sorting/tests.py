from .models     import HouseQuestion, HouseChoice

from django.test import Client, TestCase

class HouseQuestionTest(TestCase):

    def setUp(self):
        HouseQuestion.objects.create(
            id       = 1,
            question = 'question',
        )

        HouseChoice.objects.create(
            choice      = 'choice1',
            question_id = 1
        )

        HouseChoice.objects.create(
            choice      = 'choice2',
            question_id = 1
        )

    def test_house_get_success(self):
        client   = Client()
        response = client.get('/sorting/house/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'data' : {
                    'id' : 1,
                    'question' : 'question',
                    'img_center' : None,
                    'choices' : [{
                        'choice' : 'choice1',
                        'img' : None
                    },
                                {
                        'choice' : 'choice2',
                        'img' : None
                    }]}
            }
        )
