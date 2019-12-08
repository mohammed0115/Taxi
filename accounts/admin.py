from django.contrib import admin

from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import user

class UserAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_type','phone','email','address', 'username',
        'date_of_birth','gender','lat','log','status','bloodClass','License','Vehicle'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('user_type','phone','email','address', 'username',
        'date_of_birth','gender','lat','log','status','bloodClass','License','Vehicle')}),
    )
    list_display = ['id', 'user_type','phone','email','address', 'username',
        'date_of_birth','gender','lat','log','status','bloodClass','License','Vehicle']
    # list_filter = ['User', 'owner']
    # readonly_fields = ('key',)
    
    

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(user, UserAdmin)