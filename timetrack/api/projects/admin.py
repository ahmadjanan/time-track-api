from django.contrib import admin

from api.projects.models import Project, ProjectMember, TimeLog


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Project Model Django Admin configuration
    """
    list_display = ('uuid', 'name', 'owner', 'description')
    search_fields = ('uuid', 'name', 'owner__username', 'description')
    list_filter = ('uuid', 'owner',)
    readonly_fields = ('uuid', )

    fieldsets = (
        ('Details', {
            'fields': ('name', 'description', 'uuid', )
        }),
        ('Ownership', {
            'fields': ('owner',)
        })
    )


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    """
    ProjectMember Model Django Admin configuration
    """
    list_display = ('uuid', 'project', 'user', 'status', )
    search_fields = ('uuid', 'project__name', 'user__username', 'status', )
    list_filter = ('uuid', 'user', 'project', )
    readonly_fields = ('uuid', )

    fieldsets = (
        ('Details', {
            'fields': ('uuid', )
        }),
        ('Membership', {
            'fields': ('project', 'user', 'status', )
        })
    )


@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    """
    TimeLog Model Django Admin configuration
    """
    list_display = ('uuid', 'member', 'start_time', 'end_time', )
    search_fields = ('uuid', 'member', )
    list_filter = ('uuid', )
    readonly_fields = ('uuid', )

    fieldsets = (
        ('Details', {
            'fields': ('uuid', 'description', 'member', )
        }),
        ('Log', {
            'fields': ('start_time', 'end_time', )
        })
    )
