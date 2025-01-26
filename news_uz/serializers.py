from rest_framework import serializers

from news_uz.models import NewsUz, PhotoUz, GalleryUz, ProvisionUz, ResolutionUz, GovernanceUz, ConnectionUz


class NewsUzSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsUz
        fields = ['id', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None

# Photo Serializer
class PhotoUzSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoUz
        fields = ['id', 'image', 'uploaded_at']

# Gallery Serializer
class GalleryUzSerializer(serializers.ModelSerializer):
    photos = PhotoUzSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryUz
        fields = ['id', 'title', 'created_at', 'photos']


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