from rest_framework import serializers
from .models import ArchiveQqc, PhotoQqc, ConnectionQqc, GovernanceQqc, ResolutionQqc, ProvisionQqc


class PhotoQqcSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoQqc
        fields = ['id', 'image', 'uploaded_at']

class ArchiveQqcSerializer(serializers.ModelSerializer):
    photos = PhotoQqcSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ArchiveQqc
        fields = ['id', 'type', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url', 'created_at', 'photos']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None


class ConnectionQqcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionQqc
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceQqcSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceQqc
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionQqcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionQqc
        fields = ['id', 'title', 'link']

class ProvisionQqcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionQqc
        fields = ['id', 'title', 'link']
