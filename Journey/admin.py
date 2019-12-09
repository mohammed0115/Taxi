from django.contrib import admin

# Register your models here.
from Journey.models import Journey
from import_export.admin import ImportExportActionModelAdmin

class JourneyAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    
    fields = (
        'startLat','startLon','endLat','endLon', 'price','distance',
        'starttime','EndTime','Journey_type','status','Categories','user'
    )
    list_display = ['id','startLat','startLon','endLat','endLon', 'price','distance',
        'starttime','EndTime','Journey_type','status','Categories','user']
admin.site.register(Journey, JourneyAdmin)