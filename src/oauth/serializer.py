from rest_framework import serializers

from ..oauth import models


class GoogleAuth(serializers.Serializer):
    """Google data serialization
    """
    email = serializers.EmailField()
    token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ['avatar', 'country', 'bio', 'display_name', 'city']


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialLink
        fields = ['id', 'link']


class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = ['id', 'avatar', 'country', 'bio',
                  'display_name', 'city', 'social_links']
