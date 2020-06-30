
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name= 'login')
]
