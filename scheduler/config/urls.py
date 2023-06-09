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
from scheduling.views import add_course, course_list, delete_course, update_course, get_course_json, add_room, update_room, delete_room, room_list_json
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('activation/<uidb64>/<token>/',
         activate_account, name='activate_account'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('update-profile/<str:username>/', update_profile, name='update_profile'),
    path('profile-updated/', profile_updated, name='profile_updated'),
    path('add_course/', add_course, name='add_course'),
    path('course_list/', course_list, name='course_list'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    path('update_course/<int:course_id>/', update_course, name='update_course'),
    path('get_course_json/', get_course_json, name='get_course_json'),
    path('add_room/', add_room, name='add_room'),
    path('update_room/<int:room_id>/', update_room, name='update_room'),
    path('delete_room/<int:room_id>/', delete_room, name='delete_room'),
    path('room_list_json/', room_list_json, name='room_list_json'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
