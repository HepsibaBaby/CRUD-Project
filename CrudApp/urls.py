from django.urls import path

from CrudApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginview',views.loginview,name='loginview'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentview',views.studentview,name='studentview')
]