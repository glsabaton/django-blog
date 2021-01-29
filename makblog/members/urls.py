from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

    # path('password/', auth_view.PasswordChangeView.as_view(
    #    template_name='registration/password-change.html')),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', views.password_success, name='password_succes'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(),
         name='show_profile_page'),
    path('edit_profile_page/<int:pk>/',
         EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/',
         CreateProfilePageView.as_view(), name='create_profile_page'),
]
