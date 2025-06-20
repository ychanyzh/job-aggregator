# Generated by Django 5.2.2 on 2025-06-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('salary', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('source', models.CharField(max_length=100)),
                ('date_posted', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
