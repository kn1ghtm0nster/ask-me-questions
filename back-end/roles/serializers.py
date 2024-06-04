from rest_framework import serializers
from api_v1.models import Role


class RoleSerializer(serializers.ModelSerializer):
    """Serializer class for incoming Role information.

    """
