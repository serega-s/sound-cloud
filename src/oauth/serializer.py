from rest_framework import serializers

class GoogleAuth(serializers.Serializer):
    """Google data serialization
    """
    email = serializers.EmailField()
    token = serializers.CharField()