from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('contact',views.Contact.as_view(),name='contact'),
    path('about/us',views.About.as_view(),name='about'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('login',views.LoginView.as_view(),name='login'),
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('profile/user',views.UpdateProfileView.as_view(),name='profile'),
]
