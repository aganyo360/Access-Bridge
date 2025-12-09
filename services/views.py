from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Service
from .serializers import ServiceSerializer
from django.shortcuts import render


class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()

        city = self.request.query_params.get("city")
        accessibility = self.request.query_params.get("accessibility")
        search = self.request.query_params.get("search")

        if city:
            qs = qs.filter(city__iexact=city)

        if accessibility:
            qs = qs.filter(accessibility__icontains=accessibility)

        if search:
            qs = qs.filter(
                name__icontains=search
            ) | qs.filter(description__icontains=search)

        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().created_by:
            raise PermissionError("Not allowed to update this service.")
        return super().perform_update(serializer)


def home(request):
    return render(request, "home.html")


def map_view(request):
    return render(request, 'services/map.html')

def service_detail(request, id):
    return render(request, "services/service_detail.html")

def services_page(request):
    return render(request, "services.html")

# ORGANIZATION PAGE

def organizations_page(request):
    return render(request, "organizations.html")

