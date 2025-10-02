from django.contrib import admin
from .models import Biography, Service, Logos, Project, Achievement, Skill, HeadingText, Email, ExtraText, AboutWork, SuccessStory, SocialLink

class ProjectAdmin(admin.ModelAdmin):
  # Define field under a Pre-defined Title
  fieldsets = [
    (None, {'fields': ['title', 'category', 'description', 'image']}),
    ('More details', {'fields': ['date', 'link', 'github_link']})
  ]

  list_display = [
    'title',
    'category',
    'description',
    'date',
  ]

class EmailAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'email',
    'message',
    'date'
  ]

  # add a filter by email
  list_filter = [
    'email',
    'date',
  ]

  # add a search field by name
  search_fields = [
    'name',
    'email',
  ]
  

class SocialLinkAdmin(admin.ModelAdmin):
  list_display = [
    'platform',
    'url',
    'icon'
  ]

class SuccssStoryAdmin(admin.ModelAdmin):
  # Defines the field to display
  list_display = [
    'success_count',
    'success_description',
  ]


# Register your models here.
admin.site.register(Biography)
admin.site.register(Service)
admin.site.register(Logos)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement)
admin.site.register(Skill)
admin.site.register(HeadingText)
admin.site.register(Email, EmailAdmin)
admin.site.register(ExtraText)
admin.site.register(AboutWork)
admin.site.register(SuccessStory, SuccssStoryAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)