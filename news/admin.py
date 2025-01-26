from django.contrib import admin
from .models import News, Gallery, Photo, Connection, Governance, Resolution, Provision


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Number of empty photo fields displayed by default
    fields = ['image', 'uploaded_at']
    readonly_fields = ['uploaded_at']  # Make 'uploaded_at' read-only


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']  # Display these fields in the list view
    search_fields = ['title']  # Enable search by title
    inlines = [PhotoInline]  # Add inline management for photos


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery', 'image', 'uploaded_at']  # Display these fields in the list view
    list_filter = ['gallery']  # Add a filter by gallery
    search_fields = ['gallery__title']  # Enable search by gallery title


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'added_date']  # Display these fields in the list view
    search_fields = ['title', 'pre_description', 'author']  # Enable search by title and author
    list_filter = ['added_date']  # Add a filter by added_date


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
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


@admin.register(Governance)
class GovernanceAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'working_hours', 'email_post']
    search_fields = ['fullname', 'position', 'email_post']
    list_filter = ['working_hours']

@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']


@admin.register(Provision)
class ProvisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']