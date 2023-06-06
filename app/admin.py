from django.contrib import admin
from .models import Category, Tool, \
    Post, About, Project, Service, \
    SocialLink, ProfileData


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    ordering = ("-views_count",)


admin.site.register(About)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Tool)
admin.site.register(SocialLink)
admin.site.register(ProfileData)

