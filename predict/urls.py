from django.urls import URLPattern, path
from predict import views

urlpatterns = [
    path('',views.view,name='view'),
    # path('register.html',views.register,name='register'),
    path('login.html',views.login,name='login'),
    path('user.html',views.user,name='user'),
    path('admin.html',views.admin,name='admin'),
    path('adddetails.html',views.add_det,name='adddetails'),
    path('siup.html',views.siup,name='siup'),
    path('slog.html',views.sign,name='sign'),
    path('userview.html',views.userview,name='userview'),
    path('about.html',views.aboutview,name='aboutview'),
    path('simple_function', views.simple_function,name='simple_function'),
    path('verify.html',views.verify,name='verify'),

    
]