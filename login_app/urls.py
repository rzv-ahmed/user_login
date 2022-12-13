

from django.contrib import admin
from django.urls import path
from . import views

app_name='login_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.login_page, name='user_login'),
    path('logged/', views.logged, name='logged'),
    path('logout/', views.logout, name='logout'),
    

]
