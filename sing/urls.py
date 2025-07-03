from django.urls import path
from .views import BaseRegisterView, become_author, logout_page, login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', BaseRegisterView.as_view(), name='register'),
    path('become-author/', become_author, name='become_author'),
] 