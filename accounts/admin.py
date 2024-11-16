from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # Grant view access to staff users.
    def has_module_permission(self, request):
        return request.user.is_staff or request.user.is_superuser
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser
    


    fieldsets = [
        ("User Info", {"fields":["username","national_id","first_name", "last_name", "is_staff", "is_superuser"], "classes":["colaple"]}),
    ]





    # def get_form(slef, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if not request.user.is_superuser:
    #         form.base_fields['is_superuser'].disabled=True
    #     return form

admin.site.register(CustomUser, CustomUserAdmin)