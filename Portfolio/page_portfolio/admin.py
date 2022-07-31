from django.contrib import admin
from .models import ProjectMiniature, Project

# Register your models here.

class ProjectMiniatureAdmin(admin.ModelAdmin):
    readonly_field = ("created", "updated")
    list_display = ('title', 'order')


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(ProjectMiniature, ProjectMiniatureAdmin)
admin.site.register(Project, ProjectAdmin )





