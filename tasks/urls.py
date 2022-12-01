from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path("Inicio", views.World_gamer, name="World_gamer"),
    path("Dota", views.Dota, name="Dota"),
    path("GTA5", views.GTAV, name="GTA5"),
    path("Fornite", views.Fornite, name="Fornite"),
    
    path("PUGB", views.PUGB, name="PUBG"),
    path("Minecraft", views.Minecraft, name="Minecraft"),
    path("Roblox", views.Roblox, name="Roblox"),
    path("login/", views.login, name="login"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("logout_user", views.logout_user, name="logout_user"),
]
