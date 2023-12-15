from django.urls import path
from . import views


#creamos el urls para la pag 
urlpatterns = [
    path('', views.home, name= 'home'),
    #path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout')
]
