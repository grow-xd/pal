from django.urls import path
from .views import UserProfileListCreateView, GroupListCreateView, ListAllGroupsView, list_friends, create_group, join_group, add_friend, list_loc_friends

urlpatterns = [
    path('userprofiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('groups/all/', ListAllGroupsView.as_view(), name='list-all-groups'),
    path('userprofiles/<int:user_id>/friends/', list_friends, name='list-friends'),
    path('userprofiles/<int:user_id>/friends/<str:loc>', list_loc_friends, name='list-loc-friends'),
    path('groups/create/', create_group, name='create-group'),
    path('groups/join/', join_group, name='join-group'),
    path('add_friend/<str:username>/', add_friend, name='add_friend'),

]
