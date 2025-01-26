from rest_framework import serializers
from .models import NewsQa, PhotoQa, GalleryQa, ConnectionQa, GovernanceQa, ResolutionQa, ProvisionQa


class NewsQaSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsQa
        fields = ['id', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None

# Photo Serializer
class PhotoQaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoQa
        fields = ['id', 'image', 'uploaded_at']

# Gallery Serializer
class GalleryQaSerializer(serializers.ModelSerializer):
    photos = PhotoQaSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryQa
        fields = ['id', 'title', 'created_at', 'photos']


class ConnectionQaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionQa
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceQaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceQa
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionQaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionQa
        fields = ['id', 'title', 'link']

class ProvisionQaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionQa
        fields = ['id', 'title', 'link']
