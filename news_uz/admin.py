from django.contrib import admin
from .models import NewsUz, GalleryUz, PhotoUz, ConnectionUz, GovernanceUz, ResolutionUz, ProvisionUz


class PhotoInline(admin.TabularInline):
    model = PhotoUz
    extra = 1  # Number of empty photo fields displayed by default
    fields = ['image', 'uploaded_at']
    readonly_fields = ['uploaded_at']  # Make 'uploaded_at' read-only


@admin.register(GalleryUz)
class GalleryUzAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']  # Display these fields in the list view
    search_fields = ['title']  # Enable search by title
    inlines = [PhotoInline]  # Add inline management for photos


@admin.register(PhotoUz)
class PhotoUzAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery', 'image', 'uploaded_at']  # Display these fields in the list view
    list_filter = ['gallery']  # Add a filter by gallery
    search_fields = ['gallery__title']  # Enable search by gallery title


@admin.register(NewsUz)
class NewsUzAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'added_date']  # Display these fields in the list view
    search_fields = ['title', 'pre_description', 'author']  # Enable search by title and author
    list_filter = ['added_date']  # Add a filter by added_date


@admin.register(ConnectionUz)
class ConnectionUzAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'postal_code',
        'email_address',
        'working_hours',
        'first_phone',
        'second_phone',
        'has_embed_map'
    ]
    search_fields = ['title', 'email_address', 'postal_code']
    list_filter = ['working_hours']

    def has_embed_map(self, obj):
        """Display whether an embed map is available"""
        return bool(obj.embed_map_html)
    has_embed_map.short_description = "Has Embed Map"
    has_embed_map.boolean = True  # Show as a boolean in the admin panel


@admin.register(GovernanceUz)
class GovernanceUzAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'working_hours', 'email_post']
    search_fields = ['fullname', 'position', 'email_post']
    list_filter = ['working_hours']

@admin.register(ResolutionUz)
class ResolutionUzAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']


@admin.register(ProvisionUz)
class ProvisionUzAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']