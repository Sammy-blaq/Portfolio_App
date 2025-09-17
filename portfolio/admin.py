from django.contrib import admin
from .models import Biography, Service, Logos, Project, Achievement, Skill, HeadingText, Email, ExtraText

# Register your models here.
admin.site.register(Biography)
admin.site.register(Service)
admin.site.register(Logos)
admin.site.register(Project)
admin.site.register(Achievement)
admin.site.register(Skill)
admin.site.register(HeadingText)
admin.site.register(Email)
admin.site.register(ExtraText)