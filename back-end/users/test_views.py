import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
def test_signup_view():
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
