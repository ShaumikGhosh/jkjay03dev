from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('api/v1/register/', views.SignupUser.as_view()),
    path('api/v1/login/', views.LoginUser.as_view()),
    path('api/v1/logout/', views.LogoutUser.as_view()),
    path('api/v1/create-post/', views.CreatePost.as_view()),
    path('api/v1/get-single-post-data/<int:id>/', views.UpdatePost.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)