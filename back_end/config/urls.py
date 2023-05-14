"""
URL configuration for back_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import activate_account
from accounts.views import  UserListView, update_profile, profile_updated

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('activation/<uidb64>/<token>/',
         activate_account, name='activate_account'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('update-profile/<str:username>/', update_profile, name='update_profile'),
    path('profile-updated/', profile_updated, name='profile_updated'),    

]
