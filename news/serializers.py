from rest_framework import serializers
from .models import News, Photo, Gallery, Connection, Governance, Resolution, Provision


class NewsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None

# Photo Serializer
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'uploaded_at']

# Gallery Serializer
class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'created_at', 'photos']


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolution
        fields = ['id', 'title', 'link']

class ProvisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provision
        fields = ['id', 'title', 'link']