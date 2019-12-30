from django.contrib import admin

# Register your models here.
from Journey.models import trip
from import_export.admin import ImportExportActionModelAdmin

class JourneyAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    
    fields = (
        'startLat','startLon','endLat','endLon', 'price','distance',
        'starttime','EndTime','Journey_type','stat','Categories'
    )
    list_display = ['id','startLat','startLon','endLat','endLon', 'price','distance',
        'starttime','EndTime','Journey_type','stat','Categories',]
admin.site.register(trip, JourneyAdmin)