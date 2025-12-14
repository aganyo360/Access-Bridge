from django.urls import path
from .views import RegisterView, MeView, ProfileUpdateView, login_view, register_view, logout_view, dashboard_redirect,user_dashboard, admin_dashboard
from rest_framework.authtoken import views as drf_views


urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="api-register"),
    path("api/me/", MeView.as_view(), name="api-me"),
    path("api/me/profile/", ProfileUpdateView.as_view(), name="api-profile"),
    path('login/', login_view, name='login'),
    path('register/',register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path("dashboard/", dashboard_redirect, name="dashboard_redirect"),
    path("dashboard/user/", user_dashboard, name="user_dashboard"),
    path("dashboard/admin/", admin_dashboard, name="admin_dashboard"),

]
