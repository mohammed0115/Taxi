from django.contrib import admin

# Register your models here.
from Vehicle.models import Vehicle
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
class VehicleAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    
    fields  = ['chassNo','plateNo','color','model','year','Categories']
    list_display = ['id','chassNo','plateNo','color','model','year','Categories']
admin.site.register(Vehicle, VehicleAdmin)