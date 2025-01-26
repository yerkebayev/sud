from rest_framework import serializers

from news_oz.models import NewsOz, PhotoOz, GalleryOz, ProvisionOz, ResolutionOz, GovernanceOz, ConnectionOz


class NewsOzSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsOz
        fields = ['id', 'title', 'pre_description', 'description', 'added_date', 'author', 'author_position', 'photo', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url
        return None

# Photo Serializer
class PhotoOzSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoOz
        fields = ['id', 'image', 'uploaded_at']

# Gallery Serializer
class GalleryOzSerializer(serializers.ModelSerializer):
    photos = PhotoOzSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryOz
        fields = ['id', 'title', 'created_at', 'photos']


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