from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("addnewuser/", views.addnewuser, name="addnewuser"),

    path("leave_create/", views.leave_create, name="leave_create"),
    path("leavemanage/", views.leavemanage, name="leavemanage"),
    path("updateleavestat/", views.updateleavestat, name="updateleavestat"),
    
    path("reimbusmentmanage/", views.reimbusmentmanage, name="reimbusmentmanage"),
    path("updatereimbusment/", views.updatereimbusment, name="updatereimbusment"),


    path("attendencemanage/", views.attendencemanage, name="attendencemanage"),
    path("employprofile/", views.employprofile, name="employprofile"),
    
    path("hrbot/", views.hrbot, name="hrbot"),
    path("chatinput/", views.chatinput, name="chatinput"),

    path('update_employee/<int:eacc_id>/', views.update_employee, name='update_employee'),

    
    path("hrnotification/", views.hrnotification, name="hrnotification"),
    path("hrmail/", views.hrmail, name="hrmail"),
  
    
    
    # for external api
    path("oneemploy/", views.oneemploy, name="oneemploy"),
    path("oneLeave/", views.oneLeave, name="oneLeave"),
    path("oneReimbusement/", views.oneReimbusement, name="oneReimbusement"),



    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register'),
  


# Old ref code


    # path("viewNodes/", views.viewNodes, name="viewNodes"),
    # path("viewNodeData/", views.viewNodeData, name="viewNodeData"),
    # path("viewclusterData/", views.viewclusterData, name="viewclusterData"),
    # path("addnode/", views.addnode, name="addnode"),
    # path("addcluster/", views.addcluster, name="addcluster"),
    # path('sensor_data/', views.sensor_data, name='sensor_data'),
    # path('read_sensor_data/', views.read_sensor_data, name='read_sensor_data'),
    # path('apikeyGen/', views.your_view_function, name='your_view_function'),

    # path("contact/", views.contact, name="ContactUs"),
    # # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),
]
