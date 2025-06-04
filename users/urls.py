from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, CustomLoggedOut, CustomLoginView


app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:logged_out'), name='logout'),
    path('logged_out/', CustomLoggedOut.as_view(), name='logged_out'),
    path('register/', RegisterView.as_view(), name='register'),
]
