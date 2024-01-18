from django.urls import path, include,re_path
from . import views

from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('chat/<int:chat_room_id>/', views.chat_room, name='chat_room'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^$', RedirectView.as_view(url='login/', permanent=False)),
    path('home/', views.home, name='home'),
    path('startchat/<int:user_id>/', views.start_chat, name='start_chat'),

]