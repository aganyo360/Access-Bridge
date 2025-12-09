from rest_framework import generics, permissions
from .models import Organization
from .serializers import OrganizationSerializer

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all().order_by('-created_at')
    serializer_class = OrganizationSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_permissions(self):
        # only creator can update
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().created_by:
            raise PermissionError("Not allowed to update this organization.")
        return super().perform_update(serializer)
