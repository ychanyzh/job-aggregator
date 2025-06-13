from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "experience",
        "date_published",
        "source",
        "is_active",
    )
    list_filter = ("location", "source", "is_active")
