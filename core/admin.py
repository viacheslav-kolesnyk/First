from django.contrib import admin
from core.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columns displayed directly in the task list table view
    list_display = ("content_summary", "created_at", "deadline", "is_done", "get_tags")

    # Filter sidebar choices for quick database querying
    list_filter = ("is_done", "created_at", "tags")

    # Text lookup capabilities across fields
    search_fields = ("content", "tags__name")

    # Allows editing completion status directly from the list page view
    list_editable = ("is_done",)

    # Handles many-to-many relationship layout cleanly inside the editor screen
    filter_horizontal = ("tags",)

    # Custom method to shorten text content preview inside rows
    def content_summary(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    content_summary.short_description = "Task Description"

    # Custom method to render associated tag items in a single cell list
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    get_tags.short_description = "Assigned Tags"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Columns displayed for managing classification labels
    list_display = ("name",)

    # Search functionality targeting specific string attributes
    search_fields = ("name",)
