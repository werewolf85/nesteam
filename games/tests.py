from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from .factories import GameFactory
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        Genre(
            name='test genre 1',
            description="test descr 1"
        ).save()

        Studio(
            name="test studio 1",
            workers_count=123,
            games_count=45
        ).save()

        data = {
            "name": "Test game 1",
            "year": 2019,
            "genre": 1,
            "studio": 1
        }

        response = self.client.post('/game-create/', data)
        self.assertEqual(response.status_code, 201)

        game = Game.objects.last()
        self.assertEqual(game.name, data["name"])
        self.assertEqual(game.year, data["year"])
        self.assertEqual(game.genre.id, data["genre"])
        self.assertEqual(game.studio.id, data["studio"])

    def test_create_game_with_wrong_data_should_fail(self):
        response = self.client.post('/game-create/', {"test1": "lorem"})
        self.assertEqual(response.status_code, 400)

    def test_create_game_via_get_request_should_return_405(self):
        data = {
            "name": "Wrong form",
            "year": 2019,
            "genre": 1,
            "studio": 1
        }
        response = self.client.get('/game-create/', data)
        self.assertEqual(response.status_code, 405)
        games_exists = Game.objects.filter(name="Wrong form").exists()
        self.assertFalse(games_exists)

class GamesTest(APITestCase):
    def setUp(self):
        self.col_1 = GameFactory()
        self.col_2 = GameFactory()
        self.col_3 = GameFactory()

    # def test_get_list_of_3_games(self):
    #     response = self.client.get('/apigame/')
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertEqual(self.col_1.name, response.data[0]["name"])
    #     # self.assertEqual(self.col_2.name, response.data[1]["name"])
    #     # self.assertEqual(self.col_3.name, response.data[2]["name"])

    def test_get_one_games(self):
        response = self.client.get(f'/apigame/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data["name"])

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_authentication(self):
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

        response = self.client.get('/apistudio/')
        self.assertEqual(response.status_code, 200)

        self.client.credentials(HTTP_AUTHORIZATION='JWT invalid-token')
        response = self.client.get('/apistudio/')
        self.assertEqual(response.status_code, 401)