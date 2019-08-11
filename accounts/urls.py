from django.urls import path
from . import views

urlpatterns = [
path('login/', views.login_user, name='login'),   
path('logout/', views.logout_user, name='logout'),
path('register/', views.register_user, name='register'),
path('profile/', views.profile_user, name='profile'),
path('edit_profile/', views.edit_profile, name='edit_profile'),
path('change_password/', views.change_password, name='change_password'),
]
 