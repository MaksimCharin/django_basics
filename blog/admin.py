from django.contrib import admin

from django.contrib import admin
from .models import BlogMessage


@admin.register(BlogMessage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'preview', 'view_counter')
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)

