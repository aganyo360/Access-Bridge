from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),

    # Organizations
    path('organizations/', views.OrganizationListView.as_view(), name='org-list'),
    path('organizations/create/', views.OrganizationCreateView.as_view(), name='org-create'),
    path('organizations/<int:pk>/edit/', views.OrganizationUpdateView.as_view(), name='org-edit'),
    path('organizations/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='org-delete'),

    # Services
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service-edit'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-delete'),
]
