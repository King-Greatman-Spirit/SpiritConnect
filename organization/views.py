from django.shortcuts import render
from django.http import HttpResponse
from .models import Organization, OrganizationOverview
# from service.models import Service, ServiceProcess
from organization_worker.models import Organization_Worker

def organization(request):
    organization = Organization.objects.get(id=1, is_church=True)
    organization_overview = OrganizationOverview.objects.get(organization=organization)
    organization_worker = Organization_Worker.objects.filter(organization=organization)
    context = {
        'organization': organization,
        'organization_overview': organization_overview,
        # 'services': services,
        'organization_worker': organization_worker,
        'navbar': organization,
    }
    return render(request, 'about.html', context)
