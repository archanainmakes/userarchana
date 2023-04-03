from django.urls import path
from bankapp import views



app_name = 'bankapp'

urlpatterns = [


    path('',views.home,name='home'),
    path('getdata', views.getdata, name="getdata"),
    path('completed', views.completed, name="completed"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('new',views.new ,name='new'),
    path('logout', views.logout, name="logout"),

]