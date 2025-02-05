from rest_framework import serializers
from .models import ArchiveQql, PhotoQql, ConnectionQql, GovernanceQql, ResolutionQql, ProvisionQql


class PhotoQqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoQql
        fields = ['id', 'image', 'uploaded_at']

class ArchiveQqlSerializer(serializers.ModelSerializer):
    photos = PhotoQqlSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ArchiveQql
        fields = ['id', 'type', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url', 'created_at', 'photos']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None


class ConnectionQqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionQql
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceQqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceQql
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionQqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionQql
        fields = ['id', 'title', 'link']

class ProvisionQqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionQql
        fields = ['id', 'title', 'link']
