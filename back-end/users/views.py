from django.contrib.auth import authenticate
from rest_framework import status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

# Create API routes here


class SignupView(APIView):
    """Class for registering a new user to the system.

    """

    def post(self, request):
        """`POST` method for creating a new user.

        Args:
            request (`str`): incoming `JSON` request object from client.
        Returns:
            `Response`: `JSON` response object with message, refresh and access tokens.

            IF `serializer` is invalid, return `Response` object with error message.
        """
        serializer = UserSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'New user created successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            data = {
                'message': 'Error creating new user',
                'errors': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Class for logging a user into the system.
    """

    def post(self, request):
        """
        `POST` method for logging a user into the system.

        IF `username` or `password` are not provided, returns `Response 400` object with error message.

        Args:
            request (`str`): incoming `JSON` request object from client.

        Returns:
            `Response`: `JSON` response object with message, refresh and access tokens.

            IF `username` or `password` are invalid, return `Response 401` object with error message.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=HTTP_401_UNAUTHORIZED)
