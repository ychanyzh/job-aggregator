from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_published = models.DateTimeField()
