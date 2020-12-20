"""
common URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 管理者用
    path('admin/', admin.site.urls),
    # API確認画面の右上ボタン用
    path('api-auth/', include('rest_framework.urls')),
    # ユーザー認証用
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    # ユーザー登録用
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    # Posts API用
    path('api/v1/posts/', include('posts.urls')),
    # Users API用
    path('api/v1/users/', include('users.urls')),
]
