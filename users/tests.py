from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):

    def setUp(self):
        '''
            Set up function for testing our code
        '''
        self.test_user = User.objects.create_user(
            username='testusername',
            email='test@test.com',
            password='testpassword',
            phone='123456789'
        )

        self.create_signup_url = reverse('create-user')

    def test_create_user(self):
        '''
        Creating user with valid data
        '''
        data = {
            'username': 'testtest',
            'email': 'testtest@test.com',
            'password': 'testtestpassword',
            'phone': '32156498798'
        }

        response = self.client.post(self.create_signup_url, data=data, format='json')

        # check of there is two user in database
        self.assertEqual(User.objects.all().count(), 2)

        # check of the new user is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check if username and email are correct
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])


    def test_create_user_with_short_password(self):
        '''
        Ensure that user will not create password less than 8 chars
        '''

        data = {
            'username': 'testtest',
            'email': 'testtest@test.com',
            'password': 'test',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        """
        Ensure that user will not create empty password
        """

        data = {
            'username': 'testtest',
            'email': 'testtest@test.com',
            'password': '',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)
    
    def test_create_user_with_long_username(self):
        """
        Ensure that user will not input a very long username
        """
        data = {
            'username': 'testtest'*30,
            'email': 'testtest@test.com',
            'password': 'test',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)
    
    def test_create_user_with_no_username(self):
        """
        Ensure that user will not input empty username
        """
        data = {
            'username': '',
            'email': 'testtest@test.com',
            'password': 'test',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)
    
    def test_create_user_with_existing_username(self):

        """
        Ensure that user will not input existing username
        """
        data = {
            'username': 'testusername',
            'email': 'testtest@test.com',
            'password': 'test',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)
    
    def test_create_user_with_wrong_email(self):
        """
        Ensure that user will not input invalid email
        """
        data = {
            'username': 'testusername',
            'email': 'testtest',
            'password': 'test',
            'phone': '32156498798'
        } 

        response = self.client.post(self.create_signup_url, data, format='json')

        # assert that status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # assert user will not be created
        self.assertEqual(User.objects.all().count(), 1)

        self.assertEqual(len(response.data['password']), 1)
        