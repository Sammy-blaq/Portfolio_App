from django.contrib import admin
from .models import Biography, Service, Logos, Project, Achievement, Skill, HeadingText, Email, ExtraText, AboutWork, SuccessStory

class ProjectAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['title', 'category', 'description', 'image']}),
    ('More details', {'fields': ['date', 'link', 'github_link']})
  ]

class EmailAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'email',
    'message'
  ]

  # add a filter by email
  list_filter = [
    'email'
  ]

  # add a search field by name
  search_fields = [
    'name'
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
admin.site.register(SuccessStory)