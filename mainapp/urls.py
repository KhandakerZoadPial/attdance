from django.urls import path
from . import views


urlpatterns=[
path('',views.home,name="home"),
path('newClass',views.newClass,name="newClass"),
path('studentPage',views.studentPage,name="studentPage"),
path('register',views.register,name="register"),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('teacherPage',views.teacherPage,name="teacherPage"),
path('classList',views.classList,name="classList"),
path('<str:classname>',views.classrecord,name="classrecord")

#path("<str:username>",views.post, name="post")

]