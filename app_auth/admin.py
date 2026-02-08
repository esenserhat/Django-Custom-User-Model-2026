from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from app_auth.models import Department, Account, Title

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name',]
    

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    def department(self, obj):
        return obj.department.name if obj.department else ""
    
    
class CustomUserAdmin(BaseUserAdmin):
    list_display        = ['full_name', 'email', 'is_admin','id', 'is_active', 'department', 'title']
    search_fields       = ['email', 'full_name']
    readonly_fields     = ['date_joined']
    fieldsets = (
        ("Personal Info",
            {"fields": ("full_name","email", "password","photo")}),
        ("Organization Info",
            {"fields": ("department", "title", "phone_gsm", "phone_internal")}),
        ("Important Dates",
            {"fields": ("date_joined",)}),
        ("Permissions",
            {"fields": ("is_staff","is_active", "is_superuser", "is_admin")}),
        ('Groups',
            {'fields': ('groups',)}),
        ('Permissions',
            {'fields': ('user_permissions',)}),
    )

    # Add User
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    ordering            = ('email',)
    filter_horizontal   = ()
    list_filter         = ()


@admin.register(Account)
class RegisterCustomUserAdmin(CustomUserAdmin):
    pass