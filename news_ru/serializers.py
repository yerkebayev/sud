from rest_framework import serializers
from .models import NewsRu, PhotoRu, GalleryRu, ConnectionRu, GovernanceRu, ResolutionRu, ProvisionRu


class NewsRuSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsRu
        fields = ['id', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None

# Photo Serializer
class PhotoRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoRu
        fields = ['id', 'image', 'uploaded_at']

# Gallery Serializer
class GalleryRuSerializer(serializers.ModelSerializer):
    photos = PhotoRuSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryRu
        fields = ['id', 'title', 'created_at', 'photos']


class ConnectionRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRu
        fields = ['id', 'title', 'postal_code', 'email_address', 'working_hours', 'first_phone', 'second_phone', 'embed_map_html']


class GovernanceRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceRu
        fields = ['id', 'position', 'fullname', 'working_hours', 'email_post', 'photo']

class ResolutionRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionRu
        fields = ['id', 'title', 'link']

class ProvisionRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvisionRu
        fields = ['id', 'title', 'link']