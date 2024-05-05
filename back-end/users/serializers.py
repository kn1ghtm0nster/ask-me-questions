from rest_framework import serializers
from api_v1.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for incoming User data.

    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'company_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """_summary_

        Args:
            validated_data (_type_): _description_

        Returns:
            _type_: _description_
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
