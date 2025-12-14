from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from organizations.models import Organization
from services.models import Service
from .forms import OrganizationForm, ServiceForm

# staff-only decorator
def staff_required(user):
    return user.is_active and user.is_staff

@user_passes_test(staff_required)
def index(request):
    # dashboard summary
    org_count = Organization.objects.count()
    svc_count = Service.objects.count()
    return render(request, 'dashboard/index.html', {'org_count': org_count, 'svc_count': svc_count})

# Generic CBVs with staff checks
method_decorator(user_passes_test(staff_required), name='dispatch')
class OrganizationListView(ListView):
    model = Organization
    template_name = 'dashboard/org_list.html'
    context_object_name = 'organizations'
    paginate_by = 20
    ordering = ['-created_at']

method_decorator(user_passes_test(staff_required), name='dispatch')
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'dashboard/org_form.html'
    success_url = reverse_lazy('dashboard:org-list')

    def form_valid(self, form):
        # optionally set created_by if model has that field
        if hasattr(form.instance, 'created_by') and self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        return super().form_valid(form)

method_decorator(user_passes_test(staff_required), name='dispatch')
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'dashboard/org_form.html'
    success_url = reverse_lazy('dashboard:org-list')

method_decorator(user_passes_test(staff_required), name='dispatch')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'dashboard/org_confirm_delete.html'
    success_url = reverse_lazy('dashboard:org-list')

# Services CRUD
method_decorator(user_passes_test(staff_required), name='dispatch')
class ServiceListView(ListView):
    model = Service
    template_name = 'dashboard/service_list.html'
    context_object_name = 'services'
    paginate_by = 20
    ordering = ['-created_at']

method_decorator(user_passes_test(staff_required), name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard:service-list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by') and self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        return super().form_valid(form)

method_decorator(user_passes_test(staff_required), name='dispatch')
class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/service_form.html'
    success_url = reverse_lazy('dashboard:service-list')

method_decorator(user_passes_test(staff_required), name='dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'dashboard/service_confirm_delete.html'
    success_url = reverse_lazy('dashboard:service-list')
