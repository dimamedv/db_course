from django.contrib import admin

from .models import Location, News, Document


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'header', 'latitude', 'longitude', 'description'
    )
    search_fields = ('user__username', 'description')
    list_filter = ('user',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
