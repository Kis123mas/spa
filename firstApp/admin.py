from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name','last_name')}),
        ('Company Position', {'fields': ('is_secretary','is_not_secretary', 'is_admin')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'phone_number')
    search_fields = ('user__email', 'phone_number')
    list_filter = ('user__is_active',)

    def user_email(self, obj):
        return obj.user.email if obj.user else "-"
    user_email.short_description = 'User Email'



class ServiceRenderedAdmin(admin.ModelAdmin):
    list_display = ['staff_name', 'amount', 'service_type', 'service_rendered', 'service_date']
    search_fields = ['staff_name__username', 'service_type']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'staff_name':
            # Only show users where is_not_secretary=True
            kwargs['queryset'] = CustomUser.objects.filter(is_not_secretary=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(ServiceRendered, ServiceRenderedAdmin)