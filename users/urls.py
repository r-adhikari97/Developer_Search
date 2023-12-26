from django.urls import  path
from . import views

urlpatterns = [
    path('',views.profiles, name='profiles'),
    path('Profile/<str:pk>', views.userProfile, name="user_profile"),

    path('logout/',views.LogoutUser,name="Logout"),
    path('login/',views.LoginUser, name="Login"),
    path('register/',views.register_user, name="Register"),
    path('account/',views.User_account, name="Account"),
    path('edit/', views.Edit_Profile, name="Edit_Profile"),

    # Skills
    path('create-skill/', views.createSkill, name="Create_Skill"),
    path('update-skill/<str:pk>', views.updateSkill, name="Update_Skill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="Delete_Skill"),

    # Inbox
    path('inbox/', views.inbox, name="Inbox")
]