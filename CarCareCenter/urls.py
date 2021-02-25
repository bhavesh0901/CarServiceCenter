"""CarCareCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CCC import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),

    path('aboutus/',views.aboutus),
    path('contactus/', views.contactus),
    path('trackorder/',views.trackorder),
    path('customerregister/',views.customerregister),
    # path('customerbase',views.customerlogin),
    path('changepassword',views.changepassword,name="changepassword"),
    path('forgotpassword',views.forgotpassword),

    # Customer Url
    path('customerbase',views.customerbase,name ='customerbase'),
    path('login',views.customerlogin,name='customerlogin'),
    path("customer_dashboard",views.customer_dashboard , name='customer_dashboard'),
    path("invoice" ,views.invoice,name='invoice'),
    path("service",views.service),
    path("customer_view_request",views.customer_view_request,name='customer_view_request'),
    path("customer_add_request",views.customer_add_request,name='customer_add_request'),
    path("customer_view_approved_request",views.customer_view_approved_request),
    path("customer_approved_request_bill",views.customer_approved_request_bill),
    path("customer_logout",views.customer_logout,name="customer_logout"),
    path("del_customer_request/<int:id>",views.del_customer_request,name='del_customer_request'),
    path('customer_feedback',views.customer_feedback),
    path("customer_profile",views.customer_profile,name='customer_profile'),
    path("cust_edit_profile",views.cust_edit_profile,name="cust_edit_profile"),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('check_otp',views.check_otp,name="check_otp"),
    path('forgotpasschange',views.forgotpasschange,name="forgotpasschange"),
    path('cust_change_pass',views.cust_change_pass,name="cust_change_pass"),

    #Mechanic URL

    path('mechaniclogin',views.mechaniclogin,name='mechaniclogin'),
    path('mechanic_base',views.mechanic_base,name='mechanic_base'),
    path('mechanicindex',views.mechanicindex,name = 'mechanicindex'),
    path('mechanic_service',views.mechanic_service,name='mechanic_service'),
    path('mechanic_feedback',views.mechanic_feedback,name='mechanic_feedback'),
    path('mechanic_update_status/<int:id>',views.mechanic_update_status,name='mechanic_update_status'),
    path('mechanic_logout',views.mechanic_logout),
    path('mechanic_leave',views.mechanic_leave,name='mechanic_leave'),
    path('mechanic_leave_form',views.mechanic_leave_form,name='mechanic_leave_form'),
    path('leave_status',views.leave_status,name='leave_status'),
    path('mechanicforgotpass',views.mechanicforgotpass,name='mechanicforgotpass'),
    path('mechanic_check_otp',views.mechanic_check_otp,name="mechanic_check_otp"),
    path('mechanicforgotpasschange',views.mechanicforgotpasschange,name="mechanicforgotpasschange"),
    path("mechanic_profile",views.mechanic_profile,name='mechanic_profile'),
    path("mech_edit_profile",views.mech_edit_profile,name="mech_edit_profile"),
    path('mech_change_pass',views.mech_change_pass,name="mech_change_pass"),
    path('career',views.career,name='career'),
    path('applyjob',views.applyjob,name='applyjob'),

    ####paytm###

    path('payment/<int:id>',views.payment,name='payment'),
    path('response',views.response, name='response'),
    path('pay_success',views.pay_success,name='pay_success'),
    path('Payment_invoice/<str:order_id>',views.GeneratePDF.as_view(),name='Payment_invoice'),
    # path('cust_invoice',views.cust_invoice,name='cust_invoice'),
    

     #Admin Url

    path('admin/',views.adminlogin,name='admin'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('show_mechanic',views.show_mechanic,name='show_mechanic'),
    path('add_mechanic',views.add_mechanic,name='add_mechanic'),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
######Paytm Payment#########

   