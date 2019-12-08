from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import APIKey

class APIKeyAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('User', 'owner', 'active'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('key', 'User', 'owner', 'active')}),
    )
    list_display = ['id', 'key', 'User', 'owner', 'active']
    list_filter = ['User', 'owner']
    readonly_fields = ('key',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(APIKey, APIKeyAdmin)