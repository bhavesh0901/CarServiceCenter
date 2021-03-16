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
    path('home', views.home),

    path('aboutus/',views.aboutus),
    path('contactus/', views.contactus),
    path('trackorder/',views.trackorder),
    path('customerregister/',views.customerregister),
    # path('customerbase',views.customerlogin),
    path('changepassword',views.changepassword,name="changepassword"),
    path('forgotpassword',views.forgotpassword),


    #==================================================#
    #              Customer Related URL                #
    #==================================================#
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
    path('customerindex',views.customerindex,name='customerindex'),
    path('sub_category/<int:id>',views.sub_category_view_customer,name='sub_category'),


    #==================================================#
    #              Mechanic Related URL                #
    #==================================================#
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


    #==================================================#
    #              Paytm Related URL                   #
    #==================================================#
    path('payment/<int:id>',views.payment,name='payment'),
    path('response',views.response, name='response'),
    path('pay_success',views.pay_success,name='pay_success'),
    path('Payment_invoice/<str:order_id>',views.GeneratePDF.as_view(),name='Payment_invoice'),
    


    #==================================================#
    #              Admin Related URL                   #
    #==================================================#
    path('admin/',views.adminlogin,name='admin'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('show_mechanic',views.show_mechanic,name='show_mechanic'),
    path('add_mechanic',views.add_mechanic,name='add_mechanic'),
    path('delete_mechanic/<int:id>',views.delete_mechanic,name='delete_mechanic'),
    path('admin_change_pass',views.admin_change_pass,name='admin_change_pass'),
    path('customer_view',views.customer_view,name='customer_view'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),
    path('customer_request',views.customer_request,name='customer_request'),
    path('admin_view_all_cusrequest',views.admin_view_all_cusrequest,name='admin_view_all_cusrequest'),
    path('admin_view_released_request',views.admin_view_released_request,name='admin_view_released_request'),
    path('admin_service',views.admin_service,name='admin_service'),
    path('admin_delete_request/<int:id>',views.admin_delete_request,name='admin_delete_request'),
    path('update_request/<int:id>',views.admin_update_cus_request,name='update_request'),
    path('admin_repair_done',views.admin_repair_done,name='admin_repair_done'),
    path('admin_release_req/<int:id>',views.admin_release_req,name='admin_release_req'),
    path('download_csv',views.download_csv,name='download_csv'),
    path('customer_payment',views.admin_view_payment,name='customer_payment'),
    path('export',views.paytm_csv,name='export'),
    path ('admin_profile',views.admin_profile,name='admin_profile'),
    path('admin_edit_profile',views.admin_edit_profile,name='admin_edit_profile'),
    path('add_admin',views.add_admin,name='add_admin'),
    path('show_admin',views.show_admin,name='show_admin'),
    path('adminforgotpass',views.adminforgotpass,name='adminforgotpass'),
    path('admin_check_otp',views.admin_check_otp,name='admin_check_otp'),
    path('adminforgotpasschange',views.adminforgotpasschange,name='adminforgotpasschange'),
    path('job_service',views.job_service,name='job_service'),
    path('job_detail',views.job_detail,name='job_detail'),
    path('add_job',views.add_job,name='add_job'),
    path('update_job/<int:id>',views.upade_job,name='update_job'),
    path('delete_job/<int:id>',views.delete_job,name='delete_job'),
    path('requirement',views.requirement,name='requirement'),
    path('delete_requirement/<int:id>',views.delete_requirement,name='delete_requirement'),
    path('leave_detail',views.leave_detail,name='leave_detail'),
    path('update_leave/<int:id>',views.update_leave,name='update_leave'),
    path('delete_leave/<int:id>',views.delete_leave,name='delete_leave'),
    path('admin_feedback',views.admin_feedback,name='admin_feedback'),
    path('delete_feedback/<int:id>',views.delete_feedback,name='delete_feedback'),
    path('admin_delete_all_req/<int:id>',views.admin_delete_all_req, name='admin_delete_all_req'),
    path('admin_contactus',views.admin_contactus,name="admin_contactus"),
    path('delete_contactus<int:id>',views.delete_contactus,name="delete_contactus"),


    path('admin_logout',views.admin_logout,name='admin_logout'),


    #Admin Spare Parts Sale

    path('admin_spare_parts',views.admin_spare_parts,name='admin_spare_parts'),
    path('category_home',views.category_home,name='category_home'),
    path('show_category',views.show_category,name='show_category'),
    path('add_category',views.add_category,name='add_category'),
    path('add_sub_category',views.add_sub_category,name='add_sub_category'),
    path('show_sub_category',views.show_sub_category,name='show_sub_category'),
    path('subcategory/<int:id>',views.sub_category_view,name='subcategory'),
    path('add_cart/<int:id>',views.add_cart,name='add_cart'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('remove_from_cart_view/<int:id>',views.remove_from_cart_view,name='remove_from_cart_view'),
    path('cust_add_cart/<int:id>',views.cust_add_cart,name='cust_add_cart'),
    path('cust_view_cart',views.cust_view_cart,name='cust_view_cart'),
    path('cust_remove_from_cart_view/<int:id>',views.cust_remove_from_cart_view,name='cust_remove_from_cart_view'),
    path('checkout',views.checkout,name='checkout'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   