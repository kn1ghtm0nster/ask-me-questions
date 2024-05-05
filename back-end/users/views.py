from rest_framework import status, serializers
from rest_framework.response import Response
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
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
