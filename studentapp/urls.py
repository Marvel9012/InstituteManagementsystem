from django.urls import path

from studentapp import views

urlpatterns=[
    path('reg',views.reg_fun,name='reg'),          #it will redirect to register.html page
    path('regdata',views.regdata_fun),             #it will create superuser account

    path('',views.log_fun,name='log'),       #it will display login.html page
    path('logdata',views.logdata_fun),    #it will read data and verify that user is super user or not

    path('home',views.home_fun,name='home'), #it will redirect to home.html page

    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.readdata_fun),    #it will insert record into student table

    path('display',views.display_fun,name='display'), #it will display student table data in diplay.html file

    path('update/<int:id>',views.update_fun,name='up'), #it will update student data

    path('delete/<int:id>',views.delete_fun,name='del'), #it will delete student record

    path('log_out',views.log_out_fun,name='log_out') #it will logout the account
]