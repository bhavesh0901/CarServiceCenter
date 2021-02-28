from django.contrib import admin
from .models import *
# import csv, datetime
from django.http import HttpResponse
# from .views import export_csv,paytm_csv



# Register your models here.
class customeradmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','gender','address','image']
admin.site.register(customer,customeradmin)

class mechanicadmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','mobile','gender','designation','salary','address','image')
admin.site.register(mechanic,mechanicadmin)

class feedbackadmin(admin.ModelAdmin):
    list_display = ('username','email','msg','date')

admin.site.register(feedback, feedbackadmin)

class cust_reqadmin(admin.ModelAdmin):
    list_display = ('category','number','name','brand','model','problem','date','cost','status')
    # actions = [export_csv]


admin.site.register(cus_request, cust_reqadmin)

class contactadmin(admin.ModelAdmin):
    list_display=('name','email','msg')

admin.site.register(contact,contactadmin)

class leaveadmin(admin.ModelAdmin):
    list_display = ('Mechanic_id','reason','from_date','to_date','status','admin_reason')

    def Mechanic_id(self,obj):
        return obj.Mechanic.fname
admin.site.register(apply_leave,leaveadmin)

class paytmadmin(admin.ModelAdmin):
    list_display = ('ORDER_ID','TXN_AMOUNT','BANKTXNID','BANKNAME','TXNDATE','STATUS')
    # actions = [paytm_csv]

class postadmin(admin.ModelAdmin):
    list_display =['post']

admin.site.register(post_name,postadmin)

class jobdescadmin(admin.ModelAdmin):
    list_display = ('image','post_name','qualification','skill','experience','job_location','salary')
admin.site.register(job_desc,jobdescadmin)

class jobadmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','dob','qualification','post_name','skills','experience','resume')

admin.site.register(job_apply, jobadmin)

admin.site.register(paytm,paytmadmin)

admin.site.site_header = "Car Care Center"

class superuseradmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','gender','address','image']
admin.site.register(superuser,superuseradmin)