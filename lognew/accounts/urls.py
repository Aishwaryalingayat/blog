from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profile/',views.profile, name='profile_url'),
    path('register/',views.register, name='register_url'),
    path('login/',LoginView.as_view(template_name='registration/login.html'), name='login_url'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('password_change/',views.PasswordChange, name='password_change_form_url'),
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset_url'),
    path('password_reset/done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),  
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),   
    #path('password_change_done/',views.PasswordChangeDoneView, name='password_change_done_url'),
    #path('post/<int:post_id>/',views.post_p, name='post_p_url'),
    path('create_post/',views.create_post, name='create_post_url'),
    path('all_post/',views.all_post, name='all_post_url'),
    path('delete_post/<int:post_id>/',views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/',views.edit_post, name='edit_post_url'),
    path('edit_profile/<int:user_id>/',views.edit_profile, name='edit_profile_url'),
    path('like_unlike_post/<int:post_id>/',views.like_unlike_post, name='like_unlike_post')
]