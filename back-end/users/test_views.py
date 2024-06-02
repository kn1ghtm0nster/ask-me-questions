# NOTE: This file contains tests for the ROUTES for the overall application.
# For those of you that are new to this, these tests are what are called Integration Tests.
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api_v1.models import User


@pytest.mark.django_db
def test_signup_view():
    """Test the signup view with valid data (AKA happy path)
    """
    client = APIClient()
    url = reverse('signup')
    data = {
        'username': 'test_user_admin',
        'email': 'testing@gmail.com',
        'password': 'thispasswordsucks',
        'company_name': 'test_corp',
        'role': None
    }

    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'message' in response.data
    assert response.data['message'] == 'New user created successfully'
    assert 'refresh' in response.data
    assert 'access' in response.data


@pytest.mark.django_db
def test_signup_with_existing_username():
    """ Test the signup view with an existing username.
    """

    User.objects.create(username='user1', email='test@gmail.com',
                        password='thispasswordsucks', company_name='test_corp')
    client = APIClient()
    url = reverse('signup')
    data = {
        'username': 'user1',
        'email': 'new@example.com',
        'password': 'somethingelse',
        'company_name': 'test_corp',
        'role': None
    }

    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert response.data['message'] == 'Error creating new user'
    assert response.data['errors']['username'] == [
        'user with this username already exists.']


@pytest.mark.django_db
def test_signup_with_existing_email():
    """Test the signup route with an existing email.
    """

    User.objects.create(username='user2', email='test@gmail.com',
                        password='thispasswordalsosucks1234', company_name='test_comp')
    client = APIClient()
    url = reverse('signup')
    data = {
        'username': 'new_user',
        'email': 'test@gmail.com',
        'password': 'newpassssssss',
        'company_name': 'test_comp',
        'role': None
    }

    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert response.data['message'] == 'Error creating new user'
    assert response.data['errors']['email'] == [
        'user with this email already exists.']


@pytest.mark.django_db
def test_signup_with_missing_username():
    """Test signup route with missing username.
    """

    client = APIClient()
    url = reverse('signup')
    bad_data = {
        'username': None,
        'email': 'test@email.com',
        'password': 'another_useless_password',
        'company_name': 'test_corp',
        'role': None
    }

    response = client.post(url, bad_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['errors']['username'] == [
        'This field may not be null.']


@pytest.mark.django_db
def test_signup_with_missing_email():
    """Test signup route with missing email.
    """

    client = APIClient()
    url = reverse('signup')
    bad_data = {
        'username': 'new_user',
        'email': None,
        'password': 'pass23333',
        'company_name': 'mckesson',
        'role': 'recruiter'
    }

    response = client.post(url, bad_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['errors']['email'] == ['This field may not be null.']


@pytest.mark.django_db
def test_signup_view_with_missing_password():
    """Test the signup view with missing password.
    """

    client = APIClient()
    url = reverse('signup')
    bad_data = {
        'username': 'new_user2',
        'email': 'test_email@email.com',
        'password': None,
        'company_name': 'test_corp',
        'role': None
    }

    response = client.post(url, bad_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['errors']['password'] == [
        'This field may not be null.']
