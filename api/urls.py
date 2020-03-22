from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('register/', views.SignupUser.as_view(), name='signup'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)