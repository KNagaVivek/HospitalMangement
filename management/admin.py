from django.contrib import admin
from .models import *

#Register your models here.
class appointmentAdmin(admin.ModelAdmin):
    list_display=['name','Phone_Number','problem','appointment_Date','Sent_Time']
    list_filter=['name','Phone_Number']
    fields = ['name','Phone_Number','problem','appointment_Date','Sent_Time']
    readonly_fields = ['Sent_Time']


admin.site.register(Modify)
admin.site.register(appointment,appointmentAdmin)
admin.site.register(pharmacy_order)
admin.site.register(cart_item)