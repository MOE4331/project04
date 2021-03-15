from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home, name="home"),
    path('login.html',views.login_user, name="login"),
    path('logout',views.logout_user, name="logout"),
    path('register',views.register_user,name ='register'),
    path('about.html',views.about, name="about"),
    path('addstock.html',views.addstock, name= "addstock"),
    path('delete/<stock_id>',views.delete , name ="delete"),
    path('sellstock.html',views.sellstock, name= "sellstock"),
    path('mystock.html',views.mystock, name= "mystock"),
    path('trade.html',views.mystock, name= "trade"),
    

]
