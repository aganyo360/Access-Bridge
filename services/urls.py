from django.urls import path
from .views import ServiceListCreateView, ServiceDetailView, map_view, service_detail,home, services_page, organizations_page
urlpatterns = [
    path('api/services/', ServiceListCreateView.as_view(), name='service-list'),
    path('api/services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('map/', map_view, name='services-map'),
    path("service/<int:id>/", service_detail, name="service-detail-page"),
    path("", home, name="home"),
    path("services/", services_page, name="services-page"),
    path("organizations/", organizations_page, name="organizations-page"),
]


