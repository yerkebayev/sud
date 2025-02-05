from rest_framework import serializers
from .models import ArchiveOz, PhotoOz, ConnectionOz, GovernanceOz, ResolutionOz, ProvisionOz


class PhotoOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoOz
        fields = ['id', 'image', 'uploaded_at']

class ArchiveOzSerializer(serializers.ModelSerializer):
    photos = PhotoOzSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ArchiveOz
        fields = ['id', 'type', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url', 'created_at', 'photos']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None


class ConnectionOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionOz
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceOz
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionOz
        fields = ['id', 'title', 'link']

class ProvisionOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionOz
        fields = ['id', 'title', 'link']
