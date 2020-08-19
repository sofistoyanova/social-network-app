from django.urls import path
from . import views

app_name='users_app'

urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('change-password/', views.change_password, name="change-password"),
]
