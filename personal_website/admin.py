from django.contrib import admin
from .models import Photo
from .models import Project
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    
admin.site.register(Photo)