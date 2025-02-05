from rest_framework import serializers
from .models import ArchiveUz, PhotoUz, ConnectionUz, GovernanceUz, ResolutionUz, ProvisionUz


class PhotoUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoUz
        fields = ['id', 'image', 'uploaded_at']

class ArchiveUzSerializer(serializers.ModelSerializer):
    photos = PhotoUzSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ArchiveUz
        fields = ['id', 'type', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url', 'created_at', 'photos']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None


class ConnectionUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionUz
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceUz
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionUz
        fields = ['id', 'title', 'link']

class ProvisionUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionUz
        fields = ['id', 'title', 'link']