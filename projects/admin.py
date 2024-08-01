from django.contrib import admin
from .models import Project, Project_Details



class ProjectDetailsInline(admin.TabularInline):
    model = Project_Details
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailsInline]

class ProjectDetailsAdmin(admin.ModelAdmin):
    pass

class ProjectCodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Project_Details, ProjectDetailsAdmin)
