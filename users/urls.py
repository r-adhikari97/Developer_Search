from django.urls import  path
from . import views

urlpatterns = [
    path('',views.profiles, name='profiles'),
    path('Profile/<str:pk>', views.userProfile, name="user_profile"),

    path('logout/',views.LogoutUser,name="Logout"),
    path('login/',views.LoginUser, name="Login")
]