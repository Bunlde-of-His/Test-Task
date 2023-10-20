from django.contrib import admin
from django.urls import path
from users.views import user_list, group_list, add_user, add_group, edit_group
from users.views import edit_user, delete_user, home_page, delete_group


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('users/', user_list, name='user_list'),
    path('groups/', group_list, name='group_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('groups/add/', add_group, name='add_group'),
    path('groups/edit/<int:group_id>/', edit_group, name='edit_group'),
    path('groups/delete/<int:group_id>/', delete_group, name='delete_group'),
]
