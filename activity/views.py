from django.shortcuts import render
from .models import Activity, Activity_Type, Testimony
from organization.models import Organization


# Create your views here.
def activity(request, activity_slug):
    organization = Organization.objects.get(id=1, is_church=True)
    # activities = Activity.objects.get(organization=organization, slug=activity_slug)
    activities = Activity.objects.all()
    context = {
        # 'organization': organization,
        'activity': activity,
    }
    return render(request, 'home.html', context)

def testimony(request):
    organization = Organization.objects.get(id=1, is_church=True)
    testimony = Testimony.objects.all()

    context = {
        'testimony': testimony,
    }

    return render(request, 'testimony.html', context)
