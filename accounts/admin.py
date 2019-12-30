from django.contrib import admin

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import user,driver,client

class UserAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    # fieldsets_admin_user = (
    #     ('Personal info', {'fields': ('user_type', 'first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_active', 'groups')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','password'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','password')}),
    )
    list_display = ['id','phone','email','address', 'username',
        'date_of_birth','gender',]
    # list_filter = ['User', 'owner']
    # readonly_fields = ('key',)
    
    

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(user, UserAdmin)






class driverAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','Vehicle','lat','lon','status','bloodClass','License','password'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','Vehicle','lat','lon','status','bloodClass','License','password')}),
    )
    list_display = ['id','phone','email','address', 'username',
        'date_of_birth','gender','Vehicle','lat','lon','status','bloodClass','License']
    # list_filter = ['User', 'owner']
    # readonly_fields = ('key',)
    
    

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(driver, driverAdmin)





class clientAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    # fieldsets_admin_user = (
    #     ('Personal info', {'fields': ('user_type', 'first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_active', 'groups')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','password'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('phone','email','address', 'username',
        'date_of_birth','gender','password')}),
    )
    list_display = ['id','phone','email','address', 'username',
        'date_of_birth','gender',]
    # list_filter = ['User', 'owner']
    # readonly_fields = ('key',)
    
    

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(client,clientAdmin)
