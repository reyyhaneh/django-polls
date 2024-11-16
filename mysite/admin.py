from django.contrib import admin

class StaffPermissionAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Grant view access to staff or superuser
        return request.user.is_staff or request.user.is_superuser

# Register StaffPermissionAdmin as the default ModelAdmin for all models
for model in admin.site._registry.values():
    if not isinstance(model, StaffPermissionAdmin):
        model.__class__ = type('NewAdmin', (model.__class__, StaffPermissionAdmin), {})