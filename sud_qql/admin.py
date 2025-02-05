from django.contrib import admin
from .models import ArchiveQql, PhotoQql, ConnectionQql, GovernanceQql, ResolutionQql, ProvisionQql


class PhotoInline(admin.TabularInline):
    model = PhotoQql
    extra = 1
    fields = ['image', 'uploaded_at']
    readonly_fields = ['uploaded_at']

@admin.register(ArchiveQql)
class ArchiveQqlAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'added_date', 'author']
    search_fields = ['title', 'pre_description', 'author']
    list_filter = ['type', 'added_date']
    inlines = [PhotoInline]

@admin.register(ConnectionQql)
class ConnectionQqlAdmin(admin.ModelAdmin):
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


@admin.register(GovernanceQql)
class GovernanceQqlAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'working_hours', 'email_post']
    search_fields = ['fullname', 'position', 'email_post']
    list_filter = ['working_hours']

@admin.register(ResolutionQql)
class ResolutionQqlAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']


@admin.register(ProvisionQql)
class ProvisionQqlAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']
