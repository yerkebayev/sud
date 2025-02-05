from django.db import models
from django.utils.timezone import now

class ArchiveUz(models.Model):
    TYPE_CHOICES = (
        ('news', 'News'),
        ('gallery', 'Gallery'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # News or Gallery
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Used for News, ignored for Gallery
    pre_description = models.CharField(max_length=2000, blank=True, null=True)  # Used for News
    added_date = models.DateTimeField(default=now, editable=False)  # Date of addition
    author = models.CharField(max_length=255, blank=True, null=True)  # Used for News
    author_position = models.CharField(max_length=255, blank=True, null=True)  # Used for News
    photo = models.ImageField(upload_to='archive_photos/', blank=True, null=True)  # Common photo field
    created_at = models.DateTimeField(auto_now_add=True)  # Used for Gallery

    def __str__(self):
        return f"{self.type.upper()}: {self.title}"


class PhotoUz(models.Model):
    archive = models.ForeignKey(ArchiveUz, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='archive_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.archive.title}"

class ConnectionUz(models.Model):
    title = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    email_address = models.EmailField()
    working_hours = models.CharField(max_length=255)
    first_phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20, blank=True, null=True)
    embed_map_html = models.TextField(blank=True, null=True)  # New field for the embed HTML code

    def __str__(self):
        return self.title


class GovernanceUz(models.Model):
    position = models.CharField(max_length=255)  # Position of the person
    fullname = models.CharField(max_length=255)  # Full name
    working_hours = models.CharField(max_length=255)  # Working hours (e.g., "9:00 AM - 5:00 PM")
    email_post = models.EmailField()  # Email address
    photo = models.ImageField(upload_to='governance_photos/', blank=True, null=True)  # Photo of the person

    def __str__(self):
        return f"{self.fullname} - {self.position}"


class ResolutionUz(models.Model):
    title = models.CharField(max_length=255)  # Title of the resolution
    link = models.URLField()  # URL link to the resolution document or page

    def __str__(self):
        return self.title

class ProvisionUz(models.Model):
    title = models.CharField(max_length=255)  # Title of the provision
    link = models.URLField()  # URL link to the provision document or page

    def __str__(self):
        return self.title

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