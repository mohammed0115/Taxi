from django.contrib import admin

# Register your models here.
from License.models import License
# Register your models here.
class LicenseAdmin(admin.ModelAdmin):
   
    fields = (
       'issueDate','expDate','License_type','issuePlace'
    )
    list_display = ['id','issueDate','expDate','License_type','issuePlace',]
admin.site.register(License, LicenseAdmin)