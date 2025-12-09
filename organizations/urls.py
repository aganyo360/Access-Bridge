from django.urls import path
from .views import OrganizationListCreateView, OrganizationDetailView

urlpatterns = [
    path("api/organizations/", OrganizationListCreateView.as_view(), name="org-list"),
    path("api/organizations/<int:pk>/", OrganizationDetailView.as_view(), name="org-detail"),
]
