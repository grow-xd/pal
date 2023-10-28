from django.urls import path
from .views import signup, user_login, get_user_info

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('get_user_info/', get_user_info, name='get-user-info'),

]
